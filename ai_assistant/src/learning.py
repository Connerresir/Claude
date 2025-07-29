import web_search
from knowledge_base import KnowledgeBase

class Learning:
    def __init__(self, user_profile, llm, username):
        self.user_profile = user_profile
        self.llm = llm
        self.kb = KnowledgeBase(username)

    def create_learning_plan(self, topic):
        # Check if the topic is already in the knowledge base
        if self.kb.get(topic):
            return self.kb.get(topic)

        learning_style = self.user_profile.get("learning_style", "visual")

        # Perform a web search to find resources
        search_results = web_search.search(topic)

        # Use the LLM to synthesize a learning plan
        prompt = f"Create a learning plan for '{topic}' for a {learning_style} learner, using the following resources:\n{search_results}"
        plan = self.llm.get_response(prompt)

        # Save the plan to the knowledge base
        self.kb.add(topic, plan)

        return plan
