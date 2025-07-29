import json
import os

class UserProfile:
    def __init__(self, username="default_user"):
        self.username = username
        self.profile_path = os.path.join("ai_assistant", "data", f"{self.username}_profile.json")
        self.profile = self.load_profile()

    def load_profile(self):
        if os.path.exists(self.profile_path):
            with open(self.profile_path, "r") as f:
                return json.load(f)
        else:
            return {}

    def save_profile(self):
        with open(self.profile_path, "w") as f:
            json.dump(self.profile, f, indent=4)

    def get(self, key, default=None):
        return self.profile.get(key, default)

    def set(self, key, value):
        self.profile[key] = value
        self.save_profile()
