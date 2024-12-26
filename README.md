# MailSender

A simple Python wrapper for sending SMTP emails. This package lets you configure:
- **TLS/SSL** or **plain** connections
- **Authentication** or unauthenticated connections
- **Attachments**, HTML/Plain text messages, CC and BCC
- And more...

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
  - [Send a Basic Email](#send-a-basic-email)
  - [Send an Email with Attachments](#send-an-email-with-attachments)
  - [Using CC and BCC](#using-cc-and-bcc)
- [License](#license)

---

## Installation

1. **Clone** or **download** this repository.
2. Navigate to the project directory (where `pyproject.toml` or `setup.py` is located).
3. Install in editable/development mode:

   ```bash
   pip install -e .
   ```

   Alternatively, if you've built a wheel or `tar.gz`:

   ```bash
   pip install dist/mailsender-0.1.0-py3-none-any.whl
   ```

Once installed, you can import it anywhere in your code:

```python
from mailsender import MailSender
```

---

## Quick Start

```python
from mailsender import MailSender

# Example instantiation of the MailSender class
mailsender = MailSender(
    smtp_server="smtp.example.com",
    port=25,          # or 587 for TLS, 465 for SSL, etc.
    use_tls=False,    # True if you want STARTTLS
    use_ssl=False,    # True if using SSL on port 465
    use_auth=False,   # True if the server requires username/password
)

# Send a simple email
mailsender.send_mail(
    sender_email="me@example.com",
    recipient_emails=["you@example.org"],
    subject="Hello World",
    body_text="This is a test email using mailsender."
)
```

---

## Configuration

When creating a `MailSender` instance, you have the following parameters:

- **smtp_server** (str): The domain or IP of your SMTP server, e.g. `"smtp.gmail.com"`, `"localhost"`, etc.
- **port** (int): The SMTP port. Often `25` or `587` (if `use_tls=True`), or `465` (if `use_ssl=True`).
- **use_tls** (bool): Set to `True` to enable STARTTLS after connecting. Typically used with port 587.
- **use_ssl** (bool): Set to `True` if you want an SSL connection from the start (SMTPS). Typically used with port 465.
- **use_auth** (bool): Set to `True` if the server requires authentication with username and password.
- **username** (str, optional): Your SMTP username (if `use_auth=True`).
- **password** (str, optional): Your SMTP password (if `use_auth=True`).

---

## Usage Examples

### Send a Basic Email

```python
from mailsender import MailSender

# Create the MailSender
mailsender = MailSender(
    smtp_server="localhost",
    port=25,
    use_tls=False,
    use_ssl=False,
    use_auth=False
)

# Send a basic text-only message
mailsender.send_mail(
    sender_email="sender@localhost",
    recipient_emails=["recipient@localhost"],
    subject="Test Email",
    body_text="Hello from mailsender!",
)
```

### Send an Email with Attachments

```python
from mailsender import MailSender

mailsender = MailSender(
    smtp_server="smtp.example.com",
    port=587,
    use_tls=True,
    use_ssl=False,
    use_auth=True,
    username="myuser",
    password="mypassword"
)

mailsender.send_mail(
    sender_email="myuser@example.com",
    recipient_emails=["recipient@example.org"],
    subject="Hello with Attachments",
    body_text="Hello, please see the attached files.",
    attachments=[
        "reports/report1.pdf",
        "/path/to/image.png"
    ]
)
```

### Using CC and BCC

```python
from mailsender import MailSender

mailsender = MailSender(
    smtp_server="smtp.example.com",
    port=25,
    use_tls=False,
    use_ssl=False,
    use_auth=False
)

mailsender.send_mail(
    sender_email="me@example.com",
    recipient_emails=["primary@example.org"],
    subject="Test CC and BCC",
    body_text="Hello, just testing CC and BCC!",
    cc_emails=["colleague@example.org"],
    bcc_emails=["secret@example.org"]
)
```

---

## License

This project is distributed under the [MIT License](LICENSE). Feel free to use it, modify it, or distribute it as you wish. See [LICENSE](LICENSE) for more information.