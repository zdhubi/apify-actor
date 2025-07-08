import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

def send_error_email(error_text):
    msg = EmailMessage()
    msg["Subject"] = "❌ Apify actor – Export selhal"
    msg["From"] = os.environ["EMAIL_FROM"]
    msg["To"] = os.environ["EMAIL_TO"]
    body = (
        f"Export selhal!\n"
        f"Důvod: {error_text}\n"
        f"Čas: {datetime.utcnow().isoformat()} UTC"
    )
    msg.set_content(body)

    with smtplib.SMTP_SSL(
        os.environ["EMAIL_HOST"],
        int(os.environ["EMAIL_PORT"])
    ) as smtp:
        smtp.login(
            os.environ["EMAIL_USER"],
            os.environ["EMAIL_PASSWORD"]
        )
        smtp.send_message(msg)

