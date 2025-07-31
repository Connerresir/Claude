from .user_profile import UserProfile
from .learning import Learning
from .email_client import EmailClient
from .social_media import Twitter, Instagram
from .conscience import check_consequences
from .credentials import Credentials
from .login import Login
from .translator import Translator
from .observer import Observer
from .thinker import Thinker
from .decider import Decider
from .actor import Actor
from .nlu import NLU
from .models import LanguageModel

import random
import os

def setup_profile(user_profile):
    print("Starting profile setup...")
    print("To help me personalize your experience, I'll ask you a few questions.")

    user_profile.set("name", input("What is your name? "))
    user_profile.set("learning_style", input("What is your preferred learning style? (e.g., visual, auditory, kinesthetic, reading/writing) "))
    user_profile.set("technical_background", input("What is your technical background? (e.g., beginner, intermediate, advanced programmer) "))
    user_profile.set("interests", input("What are some of your interests? (e.g., programming, data science, history) ").split(','))
    user_profile.set("goals", input("What are your primary goals for using this AI assistant? "))

    print("\nThank you! Your profile has been updated.")

def main():
    username = input("Enter your username: ")
    user_profile = UserProfile(username)
    llm = LanguageModel()
    learning = Learning(user_profile, llm, username)
    email_client = EmailClient(username)
    twitter = Twitter()
    instagram = Instagram()
    credentials = Credentials()
    login = Login()
    translator = Translator()
    observer = Observer(user_profile, llm, username)
    thinker = Thinker(llm)
    decider = Decider(llm, thinker)
    actor = Actor(user_profile, llm, username)
    nlu = NLU(llm)

    while True:
        prompt = input("> ")
        if prompt == "/exit":
            break

        response = llm.get_response(prompt)

        if response.startswith("learn"):
            topic = response.split(" ", 1)[1]
            plan = learning.create_learning_plan(topic)
            print(plan)
        elif response == "setup profile":
            setup_profile(user_profile)
        elif response == "read email":
            emails = email_client.get_emails()
            for email in emails:
                print(f"From: {email['from']}\nSubject: {email['subject']}\nBody: {email['body']}\n")
        elif response == "send email":
            to = input("To: ")
            subject = input("Subject: ")
            body = input("Body: ")
            warning = check_consequences("send email", {"to": to, "subject": subject, "body": body})
            if warning:
                print(warning)
                approval = input("Would you like me to do that? (y/n) ")
                if approval.lower() != "y":
                    print("Okay, I won't do that.")
                    continue
            email_client.send_email(to, subject, body)
        elif response == "propose_action":
            print("I have an idea. I can send you an email with a summary of your profile.")
            approval = input("Would you like me to do that? (y/n) ")
            if approval.lower() == "y":
                profile_summary = str(user_profile.profile)
                email_client.send_email(user_profile.get("name"), "Your Profile Summary", profile_summary)
            else:
                print("Okay, I won't do that.")
        elif response.startswith("tweet"):
            text = response.split(" ", 1)[1]
            warning = check_consequences("tweet", {"text": text})
            if warning:
                print(warning)
                approval = input("Would you like me to do that? (y/n) ")
                if approval.lower() != "y":
                    print("Okay, I won't do that.")
                    continue
            twitter.post_tweet(text)
        elif response.startswith("instagram_posts"):
            username = response.split(" ", 1)[1]
            posts = instagram.get_user_posts(username)
            for post in posts:
                print(post)
        elif response.startswith("instagram_dm"):
            parts = response.split(" ", 2)
            username = parts[1]
            message = parts[2]
            instagram.send_dm(username, message)
        elif response.startswith("instagram"):
            username = response.split(" ", 1)[1]
            info = instagram.get_user_info(username)
            print(info)
        elif response == "set credential":
            service_name = input("Service name: ")
            username = input("Username: ")
            password = input("Password: ")
            credentials.set_credential(service_name, username, password)
        elif response == "get credential":
            service_name = input("Service name: ")
            username = input("Username: ")
            password = credentials.get_credential(service_name, username)
            if password:
                print(f"Password for {username} on {service_name}: {password}")
            else:
                print(f"No password found for {username} on {service_name}")
        elif response == "login":
            service_name = input("Service name: ")
            username = input("Username: ")
            login_url = input("Login URL: ")
            username_field_id = input("Username field ID: ")
            password_field_id = input("Password field ID: ")
            submit_button_id = input("Submit button ID: ")
            driver = login.login(service_name, username, login_url, username_field_id, password_field_id, submit_button_id)
            if driver:
                # The driver is now logged in and can be used to interact with the website
                # For now, we'll just close it.
                driver.quit()
        elif response.startswith("set personality"):
            personality = response.split(" ", 2)[2]
            llm.set_personality(personality)
        elif response.startswith("translate"):
            parts = response.split(" ", 2)
            dest_lang = parts[1]
            text = parts[2]
            translated_text = translator.translate(text, dest_lang)
            print(f"Translated text: {translated_text}")
        elif response == "observe":
            observer.observe()
        elif response.startswith("think"):
            observation = response.split(" ", 1)[1]
            thinker.think(observation)
        elif response.startswith("decide"):
            goal = response.split(" ", 1)[1]
            plan = decider.decide(goal)
            print(f"Plan: {plan}")
        elif response.startswith("act"):
            plan = response.split(" ", 1)[1]
            actor.act(plan)
        elif response == "draf":
            while True:
                observer.observe()
                thinker.think("new observation")
                plan = decider.decide("achieve world peace")
                print(f"Proposed plan: {plan}")
                approval = input("Would you like me to act on this plan? (y/n) ")
                if approval.lower() == "y":
                    actor.act(plan)
                else:
                    print("Okay, I won't act on that plan.")

                # For now, we'll just break out of the loop after one iteration.
                break
        elif response.startswith("understand"):
            text = response.split(" ", 1)[1]
            intent = nlu.understand(text)
            print(f"Intent: {intent}")
        else:
            print(response)

if __name__ == "__main__":
    main()
