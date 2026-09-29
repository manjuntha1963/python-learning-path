def tool_add(first: int, second: int) -> int:
    return first + second


def simple_agent(question: str) -> str:
    if question == "2 + 3":
        return str(tool_add(2, 3))
    return "I do not have a tool for that question."


print(simple_agent("2 + 3"))
