from main import LanguageModel

def test_llm_integration():
    llm = LanguageModel()
    prompt = "Hello, world!"
    response = llm.get_response(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")

if __name__ == "__main__":
    test_llm_integration()
