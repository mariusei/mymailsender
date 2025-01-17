[![PyPI version](https://badge.fury.io/py/mymailsender.svg)](https://badge.fury.io/py/mymailsender)
[![Build Status](https://github.com/mariusei/mymailsender/actions/workflows/python-publish.yml/badge.svg)](https://github.com/mariusei/mymailsender/actions/workflows/python-publish.yml)

# MyMailSender

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
   pip install dist/mymailsender-0.1.0-py3-none-any.whl
   ```

Once installed, you can import it anywhere in your code:

```python
from mymailsender import MyMailSender
```

---

## Quick Start

```python
from mymailsender import MyMailSender

# Example instantiation of the MyMailSender class
mymailsender = MyMailSender(
    smtp_server="smtp.example.com",
    port=25,          # or 587 for TLS, 465 for SSL, etc.
    use_tls=False,    # True if you want STARTTLS
    use_ssl=False,    # True if using SSL on port 465
    use_auth=False,   # True if the server requires username/password
)

# Send a simple email
mymailsender.send_mail(
    sender_email="me@example.com",
    recipient_emails=["you@example.org"],
    subject="Hello World",
    body_text="This is a test email using mymailsender."
)
```

---

## Configuration

The `MyMailSender` class uses a `mailsender.yaml` file for default configurations. This file should be placed in the project directory and can include the following settings:

```yaml
smtp_server: "smtp.example.com"
port: 25
use_tls: false
use_ssl: false
use_auth: false
username: "your_username"
password: "your_password"
```

You can also override these settings by providing arguments when initializing the `MyMailSender` instance:

```python
from mymailsender import MyMailSender

mymailsender = MyMailSender(
    smtp_server="smtp.override.com",
    port=587,
    use_tls=True,
    # Additional overrides as needed
)
```

The available configuration parameters are:

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
from mymailsender import MyMailSender

# Create the MyMailSender
mymail = MyMailSender(
    smtp_server="localhost",
    port=25,
    use_tls=False,
    use_ssl=False,
    use_auth=False
)

# Send a basic text-only message
mymail.send_mail(
    sender_email="sender@localhost",
    recipient_emails=["recipient@localhost"],
    subject="Test Email",
    body_text="Hello from mymailsender!",
)
```

### Send an Email with Attachments

```python
from mymailsender import MyMailSender

mymail = MyMailSender(
    smtp_server="smtp.example.com",
    port=587,
    use_tls=True,
    use_ssl=False,
    use_auth=True,
    username="myuser",
    password="mypassword"
)

mymail.send_mail(
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

Configure some custom connection settings in `mailsender.yaml`:

```yaml
smtp_server: "smtp.example.com"
username: myusername
password: mypass
```

Which now allows you to initialize the `MyMailSender` instance without specifying any arguments:

```python
from mymailsender import MyMailSender

mymail = MyMailSender()

mymail.send_mail(
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