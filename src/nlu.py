from .translator import Translator
from .main import LanguageModel

class NLU:
    def __init__(self, llm):
        self.translator = Translator()
        self.llm = llm

    def understand(self, text):
        # For now, this will be a simple implementation that will just
        # translate the text to English and then pass it to the LLM.
        # In the future, this will be a more sophisticated implementation
        # that will use a dedicated NLU model.
        translated_text = self.translator.translate(text, "en")
        prompt = f"Given the following text, what is the user's intent? Text: {translated_text}"
        intent = self.llm.get_response(prompt)
        return intent
