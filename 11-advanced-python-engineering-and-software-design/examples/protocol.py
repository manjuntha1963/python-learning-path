# Purpose: Demonstrate Python Protocols for flexible interfaces.
# Protocols define what methods an object must have without requiring inheritance.

from typing import Protocol


class Retriever(Protocol):
    """
    A protocol defining what methods a retriever must have.
    
    Any class implementing a retrieve() method that matches this signature
    is compatible with code expecting a Retriever, even without inheritance.
    
    This is called "structural typing" or "duck typing".
    """
    
    def retrieve(self, query: str) -> list[str]:
        """
        Retrieve relevant items for a query.
        
        Args:
            query: The search query
        
        Returns:
            A list of matching items
        """
        ...


class Service:
    """
    A service that uses any object implementing the Retriever protocol.
    It doesn't care about the implementation, only that it has retrieve().
    """
    
    def __init__(self, retriever: Retriever):
        """
        Initialize the service with a retriever.
        The retriever must have a retrieve() method.
        """
        self.retriever = retriever
    
    def run(self, query: str) -> list[str]:
        """
        Execute a query using the retriever.
        
        Args:
            query: The search query
        
        Returns:
            Results from the retriever
        """
        return self.retriever.retrieve(query)


# Implementation 1: A simple in-memory retriever
class SimpleRetriever:
    """Searches a hardcoded dictionary."""
    
    def retrieve(self, query: str) -> list[str]:
        """Find items matching the query."""
        data = {"python": ["doc1", "doc2"], "ai": ["doc3"]}
        return data.get(query, [])


# Implementation 2: A mock retriever for testing
class MockRetriever:
    """Always returns the same results (useful for testing)."""
    
    def retrieve(self, query: str) -> list[str]:
        """Return mock results regardless of query."""
        return ["mock_result_1", "mock_result_2"]


# Both implementations work with Service because they implement the protocol
print("Protocol Example: Using different retrievers with the same service")
print()

# Use Service with SimpleRetriever
service1 = Service(SimpleRetriever())
results1 = service1.run("python")
print(f"SimpleRetriever results: {results1}")

# Use Service with MockRetriever (same code, different implementation)
service2 = Service(MockRetriever())
results2 = service2.run("python")
print(f"MockRetriever results: {results2}")

print()
print("Benefits of Protocols:")
print("  - Flexible: swap implementations without changing the service")
print("  - Testable: easy to create mock implementations")
print("  - Loosely coupled: service doesn't depend on concrete classes")
