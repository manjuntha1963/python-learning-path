# 10 - Real-World Python AI Capstone Project

This capstone combines the main ideas from the learning path into one practical application: a small document-question answering service.

The application will:

1. Accept a user question.
2. Validate the input.
3. Search a local knowledge base.
4. Build a context-aware prompt.
5. Generate a simulated answer.
6. Return a structured response.
7. Record useful logs.
8. Expose a health check.
9. Run automated tests.
10. Prepare for Docker and CI/CD deployment.

## 1. Project requirements

A good capstone starts with clear requirements.

### Functional requirements

- Users can submit a text question.
- Empty questions are rejected.
- Questions are limited to a safe length.
- Relevant documents are retrieved from a local collection.
- The response includes an answer and source information.
- The application exposes a health status.

### Non-functional requirements

- Configuration must come from environment variables.
- Secrets must not be hardcoded.
- Errors must be handled clearly.
- Important events must be logged.
- Core functions must have tests.
- The application should be easy to containerize.

### Example 1: Requirements as a Python structure

```python
requirements = {
    "input_validation": True,
    "document_retrieval": True,
    "structured_response": True,
    "logging": True,
    "automated_tests": True,
}

print(requirements)
```

**Why this is useful:**
Writing requirements first prevents the project from becoming a collection of unrelated code.

### Example 2: Define a project version

```python
APP_NAME = "knowledge-assistant"
APP_VERSION = "1.0.0"

print(f"{APP_NAME} version {APP_VERSION}")
```

### Example 3: Define supported environments

```python
SUPPORTED_ENVIRONMENTS = {"development", "staging", "production"}
environment = "development"

if environment not in SUPPORTED_ENVIRONMENTS:
    raise ValueError("Unsupported environment")

print(f"Running in {environment}")
```

## 2. Suggested project structure

```text
knowledge-assistant/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── knowledge_base.py
│   ├── prompts.py
│   ├── retrieval.py
│   ├── services.py
│   └── api.py
├── tests/
│   ├── test_retrieval.py
│   ├── test_services.py
│   └── test_validation.py
├── Dockerfile
├── .env.example
├── requirements.txt
├── main.py
└── README.md
```

### Example 1: Application entry point

```python
# main.py
from app.services import answer_question

if __name__ == "__main__":
    question = "What is Python used for?"
    print(answer_question(question))
```

### Example 2: Keep data in a separate module

```python
# app/knowledge_base.py
DOCUMENTS = [
    {"id": "python", "text": "Python is used for automation, AI, and web development."},
    {"id": "docker", "text": "Docker packages applications into portable containers."},
    {"id": "devops", "text": "DevOps combines development and operations practices."},
]
```

### Example 3: Keep prompt construction separate

```python
# app/prompts.py
ANSWER_PROMPT = """
Answer the question using only the supplied context.
Question: {question}
Context: {context}
"""


def build_prompt(question, context):
    return ANSWER_PROMPT.format(question=question, context=context)
```

### Common mistakes

#### Correct code
```python
from app.knowledge_base import DOCUMENTS

print(len(DOCUMENTS))
```

#### Wrong code
```python
from knowledge_base import DOCUMENTS

print(len(DOCUMENTS))
```

#### Error
```text
ModuleNotFoundError: No module named 'knowledge_base'
```

#### Why it happens

The module is inside the `app` package, so the package name must be included in the import.

#### Fix
```python
from app.knowledge_base import DOCUMENTS
```

## 3. Configuration

### Example 1: Configuration module

```python
# app/config.py
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
MODEL_NAME = os.getenv("MODEL_NAME", "demo-model")
MAX_QUESTION_LENGTH = int(os.getenv("MAX_QUESTION_LENGTH", "500"))
```

### Example 2: Environment file template

```text
# .env.example
ENVIRONMENT=development
MODEL_NAME=demo-model
MAX_QUESTION_LENGTH=500
LLM_API_KEY=replace-me
```

### Example 3: Validate required configuration

```python
import os


def require_api_key():
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        raise RuntimeError("LLM_API_KEY is required for the real model service")
    return api_key
```

**Why this is useful:**
The capstone can run with a simulated model locally, while production credentials remain external.

## 4. Input validation

### Example 1: Validate a question

```python
def validate_question(question, maximum_length=500):
    if not isinstance(question, str):
        raise ValueError("Question must be text")

    cleaned = question.strip()
    if not cleaned:
        raise ValueError("Question cannot be empty")
    if len(cleaned) > maximum_length:
        raise ValueError("Question is too long")

    return cleaned
```

### Example 2: Validate a request object

```python
def validate_request(request):
    if not isinstance(request, dict):
        raise ValueError("Request must be an object")
    if "question" not in request:
        raise ValueError("The question field is required")
    return validate_question(request["question"])
```

### Example 3: Use validation before processing

```python
request = {"question": "  What is DevOps?  "}
question = validate_request(request)
print(f"Validated question: {question}")
```

### Common mistakes

#### Correct code
```python
if not isinstance(question, str):
    raise ValueError("Question must be text")
```

#### Wrong code
```python
if not question.strip():
    raise ValueError("Question cannot be empty")
```

#### Error
```text
AttributeError: 'NoneType' object has no attribute 'strip'
```

#### Why it happens

The code calls a string method before checking whether the value is actually a string.

#### Fix

Check the type first, then call string methods.

## 5. Retrieval layer

Retrieval finds documents that may help answer the question.

### Example 1: Keyword retrieval

```python
from app.knowledge_base import DOCUMENTS


def retrieve_documents(query):
    words = query.lower().split()
    matches = []

    for document in DOCUMENTS:
        searchable_text = f"{document['id']} {document['text']}".lower()
        if any(word in searchable_text for word in words):
            matches.append(document)

    return matches
```

### Example 2: Format retrieved context

```python
def format_context(documents):
    return "\n".join(
        f"[{document['id']}] {document['text']}"
        for document in documents
    )
```

### Example 3: Run retrieval

```python
matches = retrieve_documents("Python automation")
context = format_context(matches)
print(context)
```

**Why this is useful:**
The context gives the answer generator facts from the application's knowledge base.

## 6. Prompt and answer service

### Example 1: Simulated model service

```python
from app.prompts import build_prompt


def generate_answer(question, context):
    prompt = build_prompt(question, context)
    return {
        "answer": f"Based on the available context: {context}",
        "prompt_used": prompt,
    }
```

### Example 2: Complete answer function

```python
from app.retrieval import retrieve_documents, format_context


def answer_question(question):
    documents = retrieve_documents(question)
    context = format_context(documents)

    if not context:
        return {
            "answer": "I could not find relevant information.",
            "sources": [],
        }

    generated = generate_answer(question, context)
    return {
        "answer": generated["answer"],
        "sources": [document["id"] for document in documents],
    }
```

### Example 3: Call the service

```python
result = answer_question("How does Docker help?" )
print(result)
```

### Common mistakes

#### Correct code
```python
context = format_context(documents)
if not context:
    print("No relevant context found")
```

#### Wrong code
```python
context = format_context(documents)
print(context.upper())
```

#### Error
```text
The application may return an empty or confusing answer.
```

#### Why it happens

The service uses context without checking whether retrieval found anything.

#### Fix

Handle the empty retrieval result before generating an answer.

## 7. Structured responses

### Example 1: Successful response

```python
response = {
    "status": "success",
    "answer": "Python supports automation.",
    "sources": ["python"],
}

print(response)
```

### Example 2: Error response

```python
error_response = {
    "status": "error",
    "error": "Question cannot be empty",
}

print(error_response)
```

### Example 3: Response validation

```python
def validate_response(response):
    if response.get("status") == "success":
        required = {"answer", "sources"}
    else:
        required = {"error"}

    missing = required - response.keys()
    if missing:
        raise ValueError(f"Missing response fields: {missing}")

    return response
```

## 8. API-style layer

### Example 1: Ask endpoint

```python
def ask_endpoint(request):
    try:
        question = validate_request(request)
        result = answer_question(question)
        return validate_response({"status": "success", **result})
    except ValueError as error:
        return {"status": "error", "error": str(error)}
```

### Example 2: Health endpoint

```python
APP_VERSION = "1.0.0"


def health_endpoint():
    return {
        "status": "healthy",
        "version": APP_VERSION,
    }
```

### Example 3: Try both endpoints

```python
print(ask_endpoint({"question": "What is Python?"}))
print(ask_endpoint({}))
print(health_endpoint())
```

## 9. Logging and error handling

### Example 1: Application logger

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("knowledge_assistant")


def log_request(question):
    logger.info("Question received with length %s", len(question))
```

### Example 2: Avoid logging secrets or full private content

```python
def log_safe_request(question):
    preview = question[:30]
    logger.info("Processing question preview: %s", preview)
```

### Example 3: Catch unexpected failures at the boundary

```python
def safe_ask_endpoint(request):
    try:
        return ask_endpoint(request)
    except Exception:
        logger.exception("Unexpected request failure")
        return {"status": "error", "error": "Internal server error"}
```

**Why this is useful:**
Users receive a safe message while developers still get diagnostic details in logs.

## 10. Automated tests

### Example 1: Test validation

```python
def test_empty_question_is_rejected():
    try:
        validate_question("")
    except ValueError as error:
        assert "empty" in str(error)
    else:
        raise AssertionError("Expected ValueError")
```

### Example 2: Test retrieval

```python
def test_python_document_is_retrieved():
    results = retrieve_documents("Python")
    ids = {document["id"] for document in results}
    assert "python" in ids
```

### Example 3: Test endpoint shape

```python
def test_success_response_has_fields():
    response = ask_endpoint({"question": "What is Python?"})
    assert response["status"] == "success"
    assert "answer" in response
    assert "sources" in response
```

### Run tests

```bash
pytest
```

### Common mistakes

#### Correct code
```python
assert response["status"] == "success"
```

#### Wrong code
```python
assert response["status"] = "success"
```

#### Error
```text
SyntaxError: cannot assign to subscript here
```

#### Why it happens

Assertions compare values with `==`; assignment uses `=`.

#### Fix
```python
assert response["status"] == "success"
```

## 11. Docker deployment

### Example 1: Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "main.py"]
```

### Example 2: Requirements file

```text
pytest
python-dotenv
```

### Example 3: Build and run

```bash
docker build -t knowledge-assistant:1.0.0 .
docker run --rm knowledge-assistant:1.0.0
```

## 12. CI/CD workflow

### Example 1: Quality gates

```python
pipeline = {
    "format": True,
    "tests": True,
    "security_scan": True,
    "build": True,
}

if all(pipeline.values()):
    print("Build can be published")
else:
    print("Build blocked")
```

### Example 2: GitHub Actions workflow

```yaml
name: Capstone checks

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest
```

### Example 3: Deployment decision

```python
tests_passed = True
image_built = True

if tests_passed and image_built:
    print("Deploy to staging")
else:
    print("Do not deploy")
```

## 13. Security checklist

- Keep API keys in environment variables or a secrets manager.
- Do not commit `.env` files containing real secrets.
- Validate request size and input type.
- Do not expose stack traces to users.
- Avoid logging passwords, API keys, or private documents.
- Restrict file types and file sizes when accepting uploads.
- Require human approval for high-impact actions.
- Keep dependencies updated and scan them regularly.

### Example: Safe secret check

```python
import os

configured = bool(os.getenv("LLM_API_KEY"))
print({"api_key_configured": configured})
```

## 14. Final project workflow

```text
Client request
    ↓
Input validation
    ↓
Request logging
    ↓
Document retrieval
    ↓
Prompt construction
    ↓
Model or simulated model service
    ↓
Response validation
    ↓
Structured API response
    ↓
Metrics and logs
```

## Practice tasks

1. Implement the project structure locally.
2. Add five documents to the knowledge base.
3. Improve retrieval so it ranks documents by matching word count.
4. Add a `confidence` field to successful responses.
5. Add tests for empty input, unknown questions, and successful retrieval.
6. Add a request identifier to logs and responses.
7. Create a Docker image and run the application locally.
8. Add a CI workflow that runs tests on every pull request.
9. Add a deployment readiness checklist.
10. Replace the simulated model service with a real provider only after adding secure configuration and output validation.

## Final debugging checklist

- Confirm imports work from the project root.
- Check that the question is a non-empty string.
- Print retrieved document IDs while debugging retrieval.
- Confirm the prompt contains the intended question and context.
- Validate response fields before returning them.
- Run unit tests before building the container.
- Check environment variables without printing their values.
- Inspect the first failing CI step rather than only the final error.
- Use health checks to separate application failures from dependency failures.

## Capstone completion criteria

The project is complete when it can:

- accept and validate a question;
- retrieve relevant local context;
- generate a structured answer;
- return useful errors;
- log safe operational information;
- pass automated tests;
- build in Docker; and
- run its checks in CI.

This capstone gives you a practical portfolio project that demonstrates Python, AI workflows, retrieval, testing, DevOps, and production-minded engineering.
