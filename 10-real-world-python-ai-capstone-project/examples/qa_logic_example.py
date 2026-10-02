# Module 10 example: document QA search logic
# This example shows a simple knowledge-base lookup used in a capstone app

DOCUMENTS = {
    "python": "Python is a programming language.",
    "ai": "AI is the science of making machines smart.",
}


def find_answer(question):
    question_lower = question.lower()
    for keyword, answer in DOCUMENTS.items():
        if keyword in question_lower:
            return answer
    return "No matching document found"


print(find_answer("What is python?"))
