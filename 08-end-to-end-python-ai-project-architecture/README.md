# 08 - End-to-End Python AI Project Architecture

A real AI application needs more than a model call. It needs clear folders, configuration, validation, logging, error handling, tests, and a safe way to connect each part.

This module shows a simple architecture for an AI or LLM application.

## 1. Project structure

A useful project can separate responsibilities into folders:

```text
ai_app/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── prompts.py
│   ├── retrieval.py
│   └── services.py
├── tests/
│   └── test_services.py
├── .env.example
├── requirements.txt
└── main.py
```

### Example 1: Separate application responsibilities

```python
# main.py
from app.services import answer_question

question = "What is Python used for?"
answer = answer_question(question)
print(answer)
```

**Why this is useful:**
The entry point stays small. Business logic can be tested and changed in separate modules.

### Example 2: Keep prompts in one module

```python
# app/prompts.py
ANSWER_PROMPT = """
Answer the question using the supplied context.
Question: {question}
Context: {context}
"""
```

### Example 3: Keep service logic in one module

```python
# app/services.py
from .prompts import ANSWER_PROMPT


def answer_question(question):
    context = "Python is used for automation, web development, and AI."
    prompt = ANSWER_PROMPT.format(question=question, context=context)
    return f"Prepared prompt: {prompt}"
```

### Common mistakes

#### Correct code
```python
from app.services import answer_question

print(answer_question("What is Python?"))
```

#### Wrong code
```python
from services import answer_question

print(answer_question("What is Python?"))
```

#### Error
```text
ModuleNotFoundError: No module named 'services'
```

#### Why it happens

Python cannot find the module because it is inside the `app` package.

#### Fix
```python
from app.services import answer_question
```

## 2. Configuration and environment variables

Secrets and environment-specific values should not be hardcoded in source code.

### Example 1: Read configuration safely

```python
# app/config.py
import os

API_KEY = os.getenv("LLM_API_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
```

### Example 2: Validate required configuration

```python
import os

api_key = os.getenv("LLM_API_KEY")

if not api_key:
    raise RuntimeError("LLM_API_KEY is not configured")

print("Configuration is ready")
```

### Example 3: Use a configuration dictionary

```python
import os

config = {
    "environment": os.getenv("ENVIRONMENT", "development"),
    "model_name": os.getenv("MODEL_NAME", "example-model"),
    "timeout_seconds": int(os.getenv("TIMEOUT_SECONDS", "30"))
}

print(config)
```

### Common mistakes

#### Correct code
```python
import os
api_key = os.getenv("LLM_API_KEY")
```

#### Wrong code
```python
api_key = "sk-example-secret-key"
```

#### Error
```text
No Python error, but this creates a security risk.
```

#### Why it happens

Hardcoded secrets can be committed to Git, copied into logs, or exposed to other people.

#### Fix

Store the value in an environment variable and keep only a placeholder in `.env.example`:

```text
LLM_API_KEY=replace-with-a-local-secret
```

## 3. Input validation

Validate user input before sending it to an AI service or database.

### Example 1: Reject empty questions

```python
def validate_question(question):
    cleaned = question.strip()
    if not cleaned:
        raise ValueError("Question cannot be empty")
    return cleaned

print(validate_question("  What is Python?  "))
```

### Example 2: Limit input length

```python
def validate_text(text, maximum_length=1000):
    if len(text) > maximum_length:
        raise ValueError("Text is too long")
    return text

print(validate_text("Short text"))
```

### Example 3: Validate a request dictionary

```python
def validate_request(request):
    if "question" not in request:
        raise ValueError("The question field is required")
    return validate_text(request["question"])

print(validate_request({"question": "Explain loops"}))
```

### Common mistakes

#### Correct code
```python
def validate_question(question):
    if not question.strip():
        raise ValueError("Question cannot be empty")
    return question
```

#### Wrong code
```python
def validate_question(question):
    return question.strip()

print(validate_question(None))
```

#### Error
```text
AttributeError: 'NoneType' object has no attribute 'strip'
```

#### Why it happens

`None` is not a string, so it does not have a `strip()` method.

#### Fix
```python
def validate_question(question):
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question must be non-empty text")
    return question.strip()
```

## 4. Error handling and logging

Production programs should handle expected failures and record useful diagnostic information.

### Example 1: Handle a missing file

```python
from pathlib import Path

try:
    content = Path("knowledge.txt").read_text()
except FileNotFoundError:
    content = "No knowledge file was found."

print(content)
```

### Example 2: Log application events

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Using development configuration")
```

### Example 3: Handle a service failure

```python
def call_model():
    raise TimeoutError("Model request timed out")

try:
    result = call_model()
except TimeoutError as error:
    print(f"Temporary service failure: {error}")
```

### Common mistakes

#### Correct code
```python
try:
    number = int("25")
except ValueError:
    number = 0
```

#### Wrong code
```python
try:
    number = int("twenty-five")
except NameError:
    number = 0
```

#### Error
```text
ValueError: invalid literal for int()
```

#### Why it happens

The raised exception is `ValueError`, but the code only catches `NameError`.

#### Fix
```python
try:
    number = int("twenty-five")
except ValueError:
    number = 0
```

## 5. Retrieval and service layers

Separating retrieval from model calls makes the application easier to test and replace.

### Example 1: Retrieval function

```python
DOCUMENTS = [
    "Python supports automation.",
    "Docker packages applications.",
    "AI models learn patterns from data."
]


def retrieve_documents(query):
    return [doc for doc in DOCUMENTS if query.lower() in doc.lower()]

print(retrieve_documents("python"))
```

### Example 2: Model service boundary

```python
def generate_answer(question, context):
    return f"Answer to '{question}' using: {context}"

print(generate_answer("What is Python?", "Python supports automation."))
```

### Example 3: Combine retrieval and generation

```python
def answer_question(question):
    matches = retrieve_documents(question)
    context = " ".join(matches) if matches else "No matching context found."
    return generate_answer(question, context)
```

## 6. API layer

An API layer receives requests, validates them, calls the service, and returns a response.

### Example 1: API-like function

```python
def ask_endpoint(request):
    question = validate_request(request)
    answer = answer_question(question)
    return {"answer": answer}

print(ask_endpoint({"question": "What is Python?"}))
```

### Example 2: Return an error response

```python
def safe_endpoint(request):
    try:
        return ask_endpoint(request)
    except ValueError as error:
        return {"error": str(error)}

print(safe_endpoint({}))
```

### Example 3: FastAPI-style route idea

```python
# This example shows the shape of a route.
# A real project would install and run FastAPI.
def health_check():
    return {"status": "healthy"}

print(health_check())
```

## 7. Testing the application

Tests check that small parts continue to work when code changes.

### Example 1: Basic assertion

```python
def add(first, second):
    return first + second

assert add(2, 3) == 5
print("Test passed")
```

### Example 2: Test validation

```python
def test_empty_question_is_rejected():
    try:
        validate_question("")
    except ValueError:
        return True
    return False

assert test_empty_question_is_rejected()
```

### Example 3: Test a response shape

```python
def test_response_has_answer():
    response = {"answer": "Python is useful."}
    assert "answer" in response


test_response_has_answer()
print("Response test passed")
```

### Common mistakes

#### Correct code
```python
def multiply(first, second):
    return first * second

assert multiply(3, 4) == 12
```

#### Wrong code
```python
def multiply(first, second):
    return first + second

assert multiply(3, 4) == 12
```

#### Error
```text
AssertionError
```

#### Why it happens

The implementation adds the values, but the test expects multiplication.

#### Fix
```python
def multiply(first, second):
    return first * second
```

## 8. Deployment preparation

### Example 1: Requirements file

```text
# requirements.txt
requests
python-dotenv
pytest
```

### Example 2: Start command

```text
python main.py
```

### Example 3: Production checklist

```python
checklist = {
    "secrets_externalized": True,
    "input_validated": True,
    "errors_logged": True,
    "tests_passing": True,
    "health_check_available": True
}

ready = all(checklist.values())
print("Ready for deployment" if ready else "Not ready for deployment")
```

## Complete request flow

A typical request can follow this path:

```text
User request
    ↓
API validation
    ↓
Retrieval of relevant context
    ↓
Prompt construction
    ↓
LLM or model service
    ↓
Output validation
    ↓
Logging and response
```

### Mini-project structure

Build an application that:

1. Receives a question.
2. Rejects empty input.
3. Searches a small document collection.
4. Builds a prompt from the question and context.
5. Produces a simulated answer.
6. Returns a structured dictionary.
7. Logs the request and result.
8. Tests the validation and retrieval functions.

## Practice tasks

1. Create the folder structure shown at the beginning of this module.
2. Write a configuration module that reads a model name and environment.
3. Add validation for missing, empty, and overly long questions.
4. Build a retrieval function over five simple documents.
5. Write tests for retrieval, validation, and response structure.
6. Add a health-check function and a deployment readiness checklist.

## Quick debugging tips

- Run the entry point from the project root so package imports work.
- Check environment variables before calling external services.
- Log the request flow without logging secrets or private user content.
- Test each layer separately before connecting the complete workflow.
- Catch only exceptions you understand; do not hide every error with a broad `except`.
- Validate model output before another system uses it.

This module brings together Python, automation, AI, LLM workflows, and DevOps practices into one maintainable project design.
