class Decider:
    def __init__(self, llm, thinker):
        self.llm = llm
        self.thinker = thinker

    def decide(self, goal):
        # For now, this will be a simple implementation that will just
        # print a message to the console. In the future, this will be
        # a more sophisticated implementation that will generate a plan
        # to achieve the goal.
        print(f"Deciding on a plan to achieve: {goal}")

        # Generate a plan
        prompt = f"Given the goal '{goal}', what is a possible plan to achieve it?"
        plan = self.llm.get_response(prompt)

        # Evaluate the utility of the plan
        prompt = f"Given the plan '{plan}', what is its utility? (0-100)"
        utility = self.llm.get_response(prompt)
        print(f"Utility: {utility}")

        # Evaluate the ethical implications of the plan
        prompt = f"Given the plan '{plan}', what are its ethical implications?"
        ethics = self.llm.get_response(prompt)
        print(f"Ethical Implications: {ethics}")

        # Evaluate the risks of the plan
        prompt = f"Given the plan '{plan}', what are its risks?"
        risks = self.llm.get_response(prompt)
        print(f"Risks: {risks}")

        return plan
