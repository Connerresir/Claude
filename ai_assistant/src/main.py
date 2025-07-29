from user_profile import UserProfile
from learning import Learning

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
    learning = Learning(user_profile)

    while True:
        command = input("> ")
        if command.startswith("/learn"):
            topic = command.split(" ", 1)[1]
            plan = learning.create_learning_plan(topic)
            print(plan)
        elif command == "/setup profile":
            setup_profile(user_profile)
        elif command == "/exit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
