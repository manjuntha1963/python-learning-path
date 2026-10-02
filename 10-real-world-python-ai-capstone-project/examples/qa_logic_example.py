# Module 10 example: document QA search logic
# This example shows a simple knowledge-base lookup used in a capstone app.
#
# Common mistake:
# Searches can fail if the code compares text using case-sensitive matching.
# Example: "Python" and "python" are not treated as the same string without normalization.
#
# Error example:
# if "python" in question:
# This may fail if the user writes "What is Python?" because the case may differ.
#
# Fix:
# Convert the question to lowercase before checking.

DOCUMENTS = {
    "python": "Python is a programming language.",
    "ai": "AI is the science of making machines smart.",
}


def find_answer(question):
    # Normalize the input to lowercase so comparisons are case-insensitive
    question_lower = question.lower()

    # Search each document keyword in the question
    for keyword, answer in DOCUMENTS.items():
        if keyword in question_lower:
            return answer

    # If nothing matches, return a clean message
    return "No matching document found"


print(find_answer("What is python?"))
print(find_answer("Tell me about AI"))
