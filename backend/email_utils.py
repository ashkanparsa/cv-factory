
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.your-email-provider.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
