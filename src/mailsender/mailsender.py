import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Optional


class MailSender:
    def __init__(
        self,
        smtp_server: str,
        port: int,
        use_tls: bool = False,
        use_ssl: bool = False,
        use_auth: bool = False,
        username: Optional[str] = None,
        password: Optional[str] = None
    ):
        """
        Wrapper for sending emails with Python's smtplib and email modules.
        
        :param smtp_server: SMTP-server, e.g. "localhost" or "smtp.mailslurp.com"
        :param port: SMTP-port, e.g. 25, 587, 465, ...
        :param use_tls: Sett til True hvis du vil kjøre STARTTLS
        :param use_ssl: Sett til True hvis du vil kjøre SSL (SMTPS)
        :param use_auth: Sett til True hvis serveren krever innlogging
        :param username: SMTP-brukernavn (valgfri)
        :param password: SMTP-passord (valgfri)
        """
        self.smtp_server = smtp_server
        self.port = port
        self.use_tls = use_tls
        self.use_ssl = use_ssl
        self.use_auth = use_auth
        self.username = username
        self.password = password

    def send_mail(
        self,
        sender_email: str,
        recipient_emails: List[str],
        subject: str,
        body_text: str,
        body_html: Optional[str] = None,
        attachments: Optional[List[str]] = None,
        cc_emails: Optional[List[str]] = None,
        bcc_emails: Optional[List[str]] = None
    ) -> None:
        """
        Sender en e-post med valgfrie vedlegg og HTML-innhold.

        :param sender_email: Avsenderens e-postadresse
        :param recipient_emails: Liste over hovedmottakere
        :param subject: Emnet for e-posten
        :param body_text: Ren-tekst-innhold
        :param body_html: (valgfritt) HTML-innhold
        :param attachments: (valgfritt) Liste over filstier for vedlegg
        :param cc_emails: (valgfritt) Liste over CC-mottakere
        :param bcc_emails: (valgfritt) Liste over BCC-mottakere
        """

        # Opprett MIME-melding
        msg = MIMEMultipart("alternative")
        msg["From"] = sender_email
        msg["To"] = ", ".join(recipient_emails)
        msg["Subject"] = subject

        if cc_emails:
            msg["Cc"] = ", ".join(cc_emails)
        # BCC settes ikke i meldingshodet

        # Legg til ren tekst
        msg.attach(MIMEText(body_text, "plain"))

        # Legg til HTML, hvis gitt
        if body_html:
            msg.attach(MIMEText(body_html, "html"))

        # Legg til vedlegg, hvis gitt
        if attachments:
            for file_path in attachments:
                with open(file_path, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                filename = file_path.split("/")[-1]  # Filnavnet uten path
                part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
                msg.attach(part)

        # Samle opp alle mottakere
        all_recipients = recipient_emails[:]
        if cc_emails:
            all_recipients.extend(cc_emails)
        if bcc_emails:
            all_recipients.extend(bcc_emails)

        # Koble til SMTP-server med rett protokoll
        if self.use_ssl:
            # SMTPS - ofte port 465
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
                self._authenticate(server)
                server.sendmail(sender_email, all_recipients, msg.as_string())
        else:
            # Ren SMTP - ofte port 25 eller 587
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.ehlo_or_helo_if_needed()

                # StartTLS hvis valgt
                if self.use_tls:
                    server.starttls()
                    server.ehlo_or_helo_if_needed()

                # Logg inn hvis valgt
                self._authenticate(server)

                # Send e-posten
                server.sendmail(sender_email, all_recipients, msg.as_string())

        print(f"E-posten er sendt til {all_recipients} med emnet '{subject}'")

    def _authenticate(self, server: smtplib.SMTP) -> None:
        """
        Hjelpefunksjon for å logge inn hvis vi har use_auth=True.
        """
        if self.use_auth and self.username and self.password:
            server.login(self.username, self.password)
