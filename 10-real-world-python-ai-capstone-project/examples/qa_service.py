# Purpose: Implement a simple document-based question answering service.
# This demonstrates the core pattern used in RAG (Retrieval-Augmented Generation).

# Knowledge base: documents the service can retrieve
# In production, this would be a vector database with thousands of documents
DOCUMENTS = {
    "python": "Python is a general-purpose programming language known for readability and simplicity.",
    "docker": "Docker packages applications and dependencies into containers for portable deployment.",
    "ai": "Artificial Intelligence enables computers to learn from data and make intelligent decisions.",
}


def answer_question(question: str) -> dict:
    """
    Answer a question by searching the knowledge base.
    
    Process:
    1. Extract keywords from the question
    2. Search the knowledge base for matching documents
    3. Return the best match with source information
    
    Args:
        question: The user's question
    
    Returns:
        A dictionary with the answer and number of sources found
    """
    # Convert question to lowercase for case-insensitive matching
    question_lower = question.lower()
    
    # Search: find documents whose keys appear in the question
    # This is a simple keyword search; production systems use embeddings
    matching_documents = [
        text
        for key, text in DOCUMENTS.items()
        if key in question_lower
    ]
    
    # Prepare the response
    if matching_documents:
        # Use the first matching document as the answer
        answer = matching_documents[0]
        status = "success"
    else:
        # No relevant documents found
        answer = "No relevant document found"
        status = "no_match"
    
    # Build the structured response
    response = {
        "question": question,
        "answer": answer,
        "status": status,
        "sources_found": len(matching_documents)
    }
    
    return response


# Test the QA service
test_questions = [
    "What is Python?",
    "Tell me about Docker",
    "Explain AI",
    "How do I use Kubernetes?",
]

print("Question Answering Service Demo")
print("=" * 50)
print()

for question in test_questions:
    result = answer_question(question)
    print(f"Q: {result['question']}")
    print(f"A: {result['answer'][:60]}..." if len(result['answer']) > 60 else f"A: {result['answer']}")
    print(f"Status: {result['status']} (found {result['sources_found']} sources)")
    print()

print("Production note:")
print("  - Replace keyword search with semantic search (embeddings)")
print("  - Use vector database (Pinecone, Weaviate, Milvus)")
print("  - Add LLM to generate natural language responses")
print("  - Implement citation/source tracking")
