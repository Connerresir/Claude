import json
import os

class KnowledgeBase:
    def __init__(self, username="default_user"):
        self.username = username
        self.data_dir = "data"
        self.kb_path = os.path.join(self.data_dir, f"{self.username}_kb.json")
        os.makedirs(self.data_dir, exist_ok=True)
        self.kb = self.load_kb()

    def load_kb(self):
        if os.path.exists(self.kb_path):
            with open(self.kb_path, "r") as f:
                return json.load(f)
        else:
            return {}

    def save_kb(self):
        with open(self.kb_path, "w") as f:
            json.dump(self.kb, f, indent=4)

    def add(self, topic, data):
        self.kb[topic] = data
        self.save_kb()

    def get(self, topic):
        return self.kb.get(topic)
