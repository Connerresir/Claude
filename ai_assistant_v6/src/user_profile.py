import json
import os

class UserProfile:
    def __init__(self, username="default_user"):
        self.username = username
        self.data_dir = "data"
        self.profile_path = os.path.join(self.data_dir, f"{self.username}_profile.json")
        os.makedirs(self.data_dir, exist_ok=True)
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
