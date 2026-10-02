# Module 04 example: simple agent logic
# This shows a decision workflow for an AI agent

# A tool is an action the agent can perform
# Here, the tool returns a simple mathematical result

def add_numbers(a, b):
    return a + b


def agent_decision(question):
    # If the question includes the word "add", use the add tool
    if "add" in question.lower():
        return add_numbers(2, 3)
    return "I can only add numbers in this example"


print(agent_decision("Please add these values"))
