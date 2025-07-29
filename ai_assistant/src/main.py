from user_profile import UserProfile
from learning import Learning
from email_client import EmailClient
from social_media import SocialMedia
from conscience import check_consequences

import random
import os

# TODO: Install the required library for your chosen LLM provider (e.g., pip install openai)
# import openai

# TODO: Set your API key as an environment variable
# openai.api_key = os.getenv("OPENAI_API_KEY")
# MODEL_NAME = "gpt-3.5-turbo"

class LanguageModel:
    def get_response(self, prompt):
        # TODO: Replace this with a real API call to your chosen LLM provider
        # response = openai.Completion.create(
        #     engine=MODEL_NAME,
        #     prompt=prompt,
        #     max_tokens=150,
        # )
        # return response.choices[0].text.strip()

        # For now, we'll just continue to simulate a response.
        if "learn" in prompt:
            return f"learn {prompt.split('learn')[1].strip()}"
        elif "setup profile" in prompt:
            return "setup profile"
        elif "read email" in prompt:
            return "read email"
        elif "send email" in prompt:
            return "send email"
        elif "tweet" in prompt:
            return f"tweet {prompt.split('tweet')[1].strip()}"

        # Propose an action with a 20% probability
        if random.random() < 0.2:
            return "propose_action"

        return f"I am a large language model. I received the following prompt: '{prompt}'"

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
    social_media = SocialMedia()

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
            social_media.post_tweet(text)
        else:
            print(response)

if __name__ == "__main__":
    main()
