import sys
import os
os.environ['QT_QPA_PLATFORM'] = 'offscreen'
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from .main import LanguageModel, setup_profile
from .user_profile import UserProfile
from .learning import Learning
from .email_client import EmailClient
from .social_media import Twitter, Instagram
from .credentials import Credentials
from .login import Login
from .translator import Translator
from .conscience import check_consequences

class AppUI(QWidget):
    def __init__(self):
        super().__init__()
        self.username = "default_user"  # TODO: Get the username from the user
        self.user_profile = UserProfile(self.username)
        self.llm = LanguageModel()
        self.learning = Learning(self.user_profile, self.llm, self.username)
        self.email_client = EmailClient(self.username)
        self.twitter = Twitter()
        self.instagram = Instagram()
        self.credentials = Credentials()
        self.login = Login()
        self.translator = Translator()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Assistant')

        # Main layout
        main_layout = QHBoxLayout()

        # Left side: Chat interface
        chat_layout = QVBoxLayout()
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_input = QLineEdit()
        self.chat_send_button = QPushButton('Send')
        self.chat_send_button.clicked.connect(self.send_message)
        chat_layout.addWidget(self.chat_history)
        chat_layout.addWidget(self.chat_input)
        chat_layout.addWidget(self.chat_send_button)
        main_layout.addLayout(chat_layout)

        # Right side: Output display and settings
        right_layout = QVBoxLayout()

        # Output display
        output_label = QLabel('Output')
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        right_layout.addWidget(output_label)
        right_layout.addWidget(self.output_display)

        # Settings area
        settings_label = QLabel('Settings')
        right_layout.addWidget(settings_label)
        # TODO: Add settings widgets here

        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)
        self.show()

    def send_message(self):
        user_message = self.chat_input.text()
        self.chat_history.append(f"You: {user_message}")
        self.chat_input.clear()
        self.process_message(user_message)

    def process_message(self, message):
        response = self.llm.get_response(message)

        if response.startswith("learn"):
            topic = response.split(" ", 1)[1]
            plan = self.learning.create_learning_plan(topic)
            self.output_display.append(plan)
        elif response == "setup profile":
            # TODO: Implement a GUI for setting up the profile
            self.output_display.append("Please set up your profile in the settings area.")
        elif response == "read email":
            emails = self.email_client.get_emails()
            for email in emails:
                self.output_display.append(f"From: {email['from']}\nSubject: {email['subject']}\nBody: {email['body']}\n")
        elif response == "send email":
            # TODO: Implement a GUI for sending emails
            self.output_display.append("Please use the email client to send emails.")
        elif response.startswith("tweet"):
            text = response.split(" ", 1)[1]
            warning = check_consequences("tweet", {"text": text})
            if warning:
                self.output_display.append(warning)
                # TODO: Get user approval from the GUI
            else:
                self.twitter.post_tweet(text)
        elif response.startswith("instagram_posts"):
            username = response.split(" ", 1)[1]
            posts = self.instagram.get_user_posts(username)
            for post in posts:
                self.output_display.append(str(post))
        elif response.startswith("instagram_dm"):
            parts = response.split(" ", 2)
            username = parts[1]
            message = parts[2]
            self.instagram.send_dm(username, message)
        elif response.startswith("instagram"):
            username = response.split(" ", 1)[1]
            info = self.instagram.get_user_info(username)
            self.output_display.append(str(info))
        elif response == "set credential":
            # TODO: Implement a GUI for setting credentials
            self.output_display.append("Please use the settings area to set your credentials.")
        elif response == "get credential":
            # TODO: Implement a GUI for getting credentials
            self.output_display.append("Please use the settings area to get your credentials.")
        elif response == "login":
            # TODO: Implement a GUI for logging in
            self.output_display.append("Please use the settings area to log in.")
        elif response.startswith("set personality"):
            personality = response.split(" ", 2)[2]
            self.llm.set_personality(personality)
        elif response.startswith("translate"):
            parts = response.split(" ", 2)
            dest_lang = parts[1]
            text = parts[2]
            translated_text = self.translator.translate(text, dest_lang)
            self.output_display.append(f"Translated text: {translated_text}")
        else:
            self.output_display.append(response)

def run_app():
    app = QApplication(sys.argv)
    ex = AppUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    import multiprocessing
    p = multiprocessing.Process(target=run_app)
    p.start()
    p.join(5)
    if p.is_alive():
        p.kill()
        p.join()
