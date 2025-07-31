from .learning import Learning
from .email_client import EmailClient
from .social_media import Twitter, Instagram

class Observer:
    def __init__(self, user_profile, llm, username):
        self.learning = Learning(user_profile, llm, username)
        self.email_client = EmailClient(username)
        self.twitter = Twitter()
        self.instagram = Instagram()

    def observe(self):
        # For now, this will be a simple implementation that will just
        # print a message to the console. In the future, this will be
        # a more sophisticated implementation that will gather information
        # from a wide variety of sources.
        print("Observing...")
