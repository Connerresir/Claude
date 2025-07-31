import anthropic
import os

class LanguageModel:
    def __init__(self):
        self.personality = "a helpful assistant"
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def set_personality(self, personality):
        self.personality = personality
        print(f"Personality set to: {self.personality}")

    def get_response(self, prompt):
        # TODO: Replace this with a real API call to your chosen LLM provider
        # full_prompt = f"You are {self.personality}. {prompt}"
        # message = self.client.messages.create(
        #     model=CLAUDE_MODEL_NAME,
        #     max_tokens=1024,
        #     messages=[
        #         {"role": "user", "content": full_prompt}
        #     ]
        # )
        # return message.content

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
        elif "set credential" in prompt:
            return "set credential"
        elif "get credential" in prompt:
            return "get credential"
        elif "login" in prompt:
            return "login"
        elif "instagram_posts" in prompt:
            return f"instagram_posts {prompt.split('instagram_posts')[1].strip()}"
        elif "instagram_dm" in prompt:
            return f"instagram_dm {prompt.split('instagram_dm')[1].strip()}"
        elif "instagram" in prompt:
            return f"instagram {prompt.split('instagram')[1].strip()}"
        elif "set personality" in prompt:
            return f"set personality {prompt.split('set personality')[1].strip()}"
        elif "translate" in prompt:
            return f"translate {prompt.split('translate')[1].strip()}"
        elif "observe" in prompt:
            return "observe"
        elif "think" in prompt:
            return f"think {prompt.split('think')[1].strip()}"
        elif "decide" in prompt:
            return f"decide {prompt.split('decide')[1].strip()}"
        elif "act" in prompt:
            return f"act {prompt.split('act')[1].strip()}"
        elif "draf" in prompt:
            return "draf"
        elif "understand" in prompt:
            return f"understand {prompt.split('understand')[1].strip()}"
        elif "analyze_me" in prompt:
            return "analyze_me"

        # Propose an action with a 20% probability
        import random
        if random.random() < 0.2:
            return "propose_action"

        return f"I am a large language model. I received the following prompt: '{prompt}'"
