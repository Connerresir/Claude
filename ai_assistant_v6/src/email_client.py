import smtplib
import imaplib
import email
import os

class EmailClient:
    def __init__(self, username):
        self.username = username
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.smtp_server = "smtp.gmail.com"  # Example for Gmail
        self.imap_server = "imap.gmail.com"  # Example for Gmail

    def send_email(self, to, subject, body):
        if not self.email_address or not self.email_password:
            print("Email credentials not set. Please set the EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
            return

        msg = email.message.EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.email_address
        msg['To'] = to

        with smtplib.SMTP_SSL(self.smtp_server, 465) as smtp:
            smtp.login(self.email_address, self.email_password)
            smtp.send_message(msg)
            print(f"Email sent to {to}: {subject}")

    def get_emails(self):
        if not self.email_address or not self.email_password:
            print("Email credentials not set. Please set the EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
            return []

        with imaplib.IMAP4_SSL(self.imap_server) as mail:
            mail.login(self.email_address, self.email_password)
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
