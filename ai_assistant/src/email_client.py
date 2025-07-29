import smtplib
import imaplib
import email
import os

# TODO: Set your email and password as environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"  # Example for Gmail
IMAP_SERVER = "imap.gmail.com"  # Example for Gmail

class EmailClient:
    def __init__(self, username):
        self.username = username

    def send_email(self, to, subject, body):
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            print("Email credentials not set. Please set the EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
            return

        msg = email.message.EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to

        with smtplib.SMTP_SSL(SMTP_SERVER, 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"Email sent to {to}: {subject}")

    def get_emails(self):
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            print("Email credentials not set. Please set the EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
            return []

        with imaplib.IMAP4_SSL(IMAP_SERVER) as mail:
            mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            mail.select("inbox")
            _, selected_emails = mail.search(None, "ALL")
            emails = []
            for num in selected_emails[0].split():
                _, data = mail.fetch(num, "(RFC822)")
                _, bytes_data = data[0]
                email_message = email.message_from_bytes(bytes_data)
                emails.append({
                    "from": email_message["from"],
                    "subject": email_message["subject"],
                    "body": self._get_body(email_message),
                })
            return emails

    def _get_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()
