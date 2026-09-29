# Purpose: Demonstrate clean architecture using layers.
# Each layer has one responsibility: data, business logic, interfaces.

class AnswerService:
    """
    The service layer contains business logic.
    It depends on a retriever (injected dependency).
    """
    
    def __init__(self, retriever):
        """
        Constructor receives the retriever as a dependency.
        This makes the service easy to test with a mock retriever.
        """
        self.retriever = retriever
    
    def answer(self, question: str) -> dict:
        """
        Answer a question by retrieving relevant sources.
        
        Process:
        1. Use the retriever to find relevant documents
        2. Build a response with the question and sources
        3. Return as a structured dictionary
        
        Args:
            question: The user's question
        
        Returns:
            A dictionary with the question and list of sources
        """
        # Call the retriever to find relevant documents
        sources = self.retriever(question)
        
        # Build the response
        response = {
            "question": question,
            "sources": sources
        }
        
        return response


# Create a simple retriever function
# In production, this would search a vector database
def simple_retriever(question: str) -> list:
    """
    A mock retriever for demonstration.
    Returns hardcoded sources regardless of the question.
    """
    return ["local-document-1", "local-document-2"]


# Create the service with the retriever
service = AnswerService(simple_retriever)

# Use the service to answer a question
result = service.answer("What is Python?")

print("Answer Service Response:")
print(f"  Question: {result['question']}")
print(f"  Sources: {result['sources']}")
print()

print("Architecture benefits:")
print("  - Easy to test: swap the retriever with a mock")
print("  - Easy to change: update the retriever without changing the service")
print("  - Clear responsibility: service focuses on logic, retriever on data")
