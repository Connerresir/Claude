import unittest
from src.language_model import LanguageModel

class TestCore(unittest.TestCase):
    def test_language_model(self):
        llm = LanguageModel()
        self.assertIsNotNone(llm)

if __name__ == '__main__':
    unittest.main()
