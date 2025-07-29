class EmailClient:
    def __init__(self, username):
        self.username = username
        self.inbox = [
            {"from": "admin@example.com", "subject": "Welcome!", "body": "Welcome to the AI assistant!"},
        ]
        self.sent = []

    def get_emails(self):
        return self.inbox

    def send_email(self, to, subject, body):
        email = {"to": to, "subject": subject, "body": body}
        self.sent.append(email)
        print(f"Email sent to {to}: {subject}")
        return email
