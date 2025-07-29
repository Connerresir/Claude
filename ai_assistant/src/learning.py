class Learning:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def create_learning_plan(self, topic):
        learning_style = self.user_profile.get("learning_style", "visual")

        plan = f"Learning plan for '{topic}' tailored for a {learning_style} learner:\n"

        if learning_style == "visual":
            plan += "1. Watch introductory videos on the topic.\n"
            plan += "2. Find and study infographics and diagrams.\n"
            plan += "3. Create mind maps to connect concepts.\n"
        elif learning_style == "auditory":
            plan += "1. Listen to podcasts or lectures on the topic.\n"
            plan += "2. Discuss the topic with others.\n"
            plan += "3. Record yourself explaining the topic and listen back.\n"
        elif learning_style == "kinesthetic":
            plan += "1. Find or create hands-on projects.\n"
            plan += "2. Use flashcards to memorize key concepts.\n"
            plan += "3. Build a small application or model.\n"
        else: # reading/writing
            plan += "1. Read articles and books on the topic.\n"
            plan += "2. Write summaries of what you've learned.\n"
            plan += "3. Take detailed notes.\n"

        return plan
