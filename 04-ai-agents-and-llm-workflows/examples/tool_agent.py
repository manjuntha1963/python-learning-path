# Purpose: Demonstrate a simple AI agent that uses tools.
# An agent is a program that takes actions to accomplish a goal.

# Define a tool: a function the agent can call
def tool_add(first: int, second: int) -> int:
    """A simple calculator tool."""
    return first + second


def simple_agent(question: str) -> str:
    """
    A basic agent that tries to answer questions.
    
    Process:
    1. Receive a question
    2. Decide which tool to use (if any)
    3. Call the tool
    4. Return the result
    """
    # Check if the question asks for addition
    if question == "2 + 3":
        # Use the calculator tool to answer
        result = tool_add(2, 3)
        return str(result)
    
    # If we don't recognize the question, say so
    return "I do not have a tool for that question."


# Test the agent
print("Question: 2 + 3")
print(f"Agent answer: {simple_agent('2 + 3')}")

print("\nQuestion: What is the weather?")
print(f"Agent answer: {simple_agent('What is the weather?')}")

print("\nIn real AI systems, agents decide which tool to use based on the question.")
print("Tools can call APIs, databases, or other services.")
