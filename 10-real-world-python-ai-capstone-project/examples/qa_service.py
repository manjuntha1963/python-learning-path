DOCUMENTS = {
    "python": "Python is a general-purpose programming language.",
    "docker": "Docker packages applications into containers.",
}


def answer_question(question: str) -> dict:
    matches = [text for key, text in DOCUMENTS.items() if key in question.lower()]
    return {"answer": matches[0] if matches else "No relevant document found", "sources": len(matches)}


print(answer_question("What is Python?"))
