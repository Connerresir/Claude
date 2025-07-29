from googletrans import Translator

class Translator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, dest_lang):
        try:
            translation = self.translator.translate(text, dest=dest_lang)
            return translation.text
        except Exception as e:
            return f"Error translating text: {e}"
