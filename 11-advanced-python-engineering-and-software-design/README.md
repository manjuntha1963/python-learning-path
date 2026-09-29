# 11 - Advanced Python Engineering and Software Design

As Python projects grow in complexity, they need careful structure, clear contracts between modules, type safety, and patterns that make large systems maintainable. Advanced engineering means writing code that other people (and future you) can understand and extend.

## 1. Object-oriented design

### Example 1: Define a class

```python
class Question:
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        return len(self.text.strip()) > 0

    def preview(self):
        return self.text[:50]


question = Question("What is Python used for?")
print(question.is_valid())
```

**Why this is useful:**
Classes bundle data and behavior together, making it easier to reason about related functionality.

### Example 2: Inheritance and specialized classes

```python
class Message:
    def __init__(self, content):
        self.content = content


class UserQuestion(Message):
    def __init__(self, content):
        super().__init__(content)
        self.source = "user"


class SystemResponse(Message):
    def __init__(self, content):
        super().__init__(content)
        self.source = "system"


question = UserQuestion("What is Python?")
response = SystemResponse("Python is a programming language.")
print(f"{question.source}: {question.content}")
```

### Example 3: Composition over inheritance

```python
class ResponseValidator:
    def validate(self, response):
        return bool(response.get("answer"))


class AnswerService:
    def __init__(self):
        self.validator = ResponseValidator()

    def answer_question(self, question):
        result = {"answer": "Python is useful."}
        if self.validator.validate(result):
            return result
        raise ValueError("Invalid response")


service = AnswerService()
print(service.answer_question("What is Python?"))
```

### Common mistakes

#### Correct code
```python
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Alice")
print(person.name)
```

#### Wrong code
```python
class Person:
    def __init__(self, name):
        name = name


person = Person("Alice")
print(person.name)
```

#### Error
```text
AttributeError: 'Person' object has no attribute 'name'
```

#### Why it happens

The local variable `name` was assigned instead of `self.name`.

#### Fix
```python
class Person:
    def __init__(self, name):
        self.name = name
```

## 2. Abstract classes and protocols

Abstract classes define an interface that subclasses must implement.

### Example 1: Abstract base class

```python
from abc import ABC, abstractmethod


class ModelService(ABC):
    @abstractmethod
    def generate_answer(self, question, context):
        pass


class OpenAIService(ModelService):
    def generate_answer(self, question, context):
        return f"Answer based on {context}"


class LocalModelService(ModelService):
    def generate_answer(self, question, context):
        return "Local model response"
```

**Why this is useful:**
Abstract classes guarantee that subclasses implement required methods.

### Example 2: Protocol (structural typing)

```python
from typing import Protocol


class Retrievable(Protocol):
    def retrieve(self, query: str) -> list:
        ...


class DocumentRetriever:
    def retrieve(self, query: str) -> list:
        return ["doc1", "doc2"]


class VectorStore:
    def retrieve(self, query: str) -> list:
        return ["vector_match_1"]


def use_retriever(retriever: Retrievable):
    results = retriever.retrieve("Python")
    return results
```

### Example 3: Interface contracts

```python
from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value):
        pass


class InMemoryCache(Cache):
    def __init__(self):
        self.store = {}

    def get(self, key: str):
        return self.store.get(key)

    def set(self, key: str, value):
        self.store[key] = value
```

## 3. Decorators

Decorators modify or enhance functions without changing their code.

### Example 1: Logging decorator

```python
def log_calls(function):
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    return a + b


print(add(2, 3))
```

**Why this is useful:**
Decorators separate cross-cutting concerns (like logging) from business logic.

### Example 2: Validation decorator

```python
def require_non_empty(function):
    def wrapper(text):
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        return function(text)
    return wrapper


@require_non_empty
def process_question(question):
    return f"Processing: {question}"


print(process_question("  What is Python?  "))
```

### Example 3: Caching decorator

```python
def cache_result(function):
    cache = {}

    def wrapper(key):
        if key not in cache:
            cache[key] = function(key)
        return cache[key]

    return wrapper


@cache_result
def expensive_lookup(query):
    print(f"Searching for {query}")
    return f"Result for {query}"


print(expensive_lookup("python"))
print(expensive_lookup("python"))
```

### Common mistakes

#### Correct code
```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper
```

#### Wrong code
```python
def my_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
```

#### Error
```text
The decorator is defined but never returned, so it doesn't wrap the function.
```

#### Why it happens

Decorators must return the wrapper function.

#### Fix

Return the wrapper from the decorator.

## 4. Context managers

Context managers handle resource setup and cleanup automatically.

### Example 1: Basic context manager

```python
class Database:
    def __enter__(self):
        print("Opening database connection")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")

    def query(self, sql):
        return f"Result of {sql}"


with Database() as db:
    print(db.query("SELECT * FROM users"))
```

**Why this is useful:**
Context managers guarantee cleanup even if an error occurs.

### Example 2: Using contextlib

```python
from contextlib import contextmanager


@contextmanager
def temporary_file():
    filename = "temp.txt"
    print(f"Creating {filename}")
    yield filename
    print(f"Deleting {filename}")


with temporary_file() as fname:
    print(f"Using {fname}")
```

### Example 3: Exception handling in context

```python
class TransactionManager:
    def __enter__(self):
        print("Starting transaction")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Rollback due to error")
            return False
        print("Commit transaction")
        return True


try:
    with TransactionManager():
        print("Doing work")
except:
    pass
```

## 5. Type hints

Type hints document what types functions expect and return.

### Example 1: Basic type hints

```python
def answer_question(question: str) -> dict:
    return {"answer": "Python is useful", "question": question}


result = answer_question("What is Python?")
print(result)
```

**Why this is useful:**
Type hints help catch errors early and make code easier to understand.

### Example 2: Complex types

```python
from typing import List, Optional, Dict


def retrieve_documents(query: str) -> List[Dict[str, str]]:
    return [
        {"id": "python", "text": "Python is a language"},
    ]


def find_user(user_id: int) -> Optional[Dict[str, str]]:
    return {"id": user_id, "name": "Alice"}


docs = retrieve_documents("python")
user = find_user(1)
```

### Example 3: Type hints for classes

```python
from typing import List


class Question:
    def __init__(self, text: str) -> None:
        self.text = text

    def is_valid(self) -> bool:
        return len(self.text.strip()) > 0

    def split_words(self) -> List[str]:
        return self.text.split()


question = Question("What is Python?")
print(question.is_valid())
```

### Common mistakes

#### Correct code
```python
def add(a: int, b: int) -> int:
    return a + b
```

#### Wrong code
```python
def add(a: int, b: int) -> int:
    return str(a + b)
```

#### Error
```text
No Python error, but the return type annotation is wrong.
```

#### Why it happens

The function signature says it returns an `int`, but it returns a `str`.

#### Fix

Return the correct type or update the annotation.

## 6. Clean architecture

Clean architecture separates an application into layers: entities, use cases, interfaces, and infrastructure.

### Example 1: Layer separation

```python
# entities.py (core business logic)
class Answer:
    def __init__(self, text: str):
        self.text = text

    def is_valid(self) -> bool:
        return len(self.text.strip()) > 0


# use_cases.py (business workflows)
def answer_user_question(question: str) -> Answer:
    return Answer("Python is useful for automation.")


# interface.py (API layer)
def handle_request(request: dict) -> dict:
    question = request["question"]
    answer = answer_user_question(question)
    return {"answer": answer.text if answer.is_valid() else "Invalid answer"}
```

### Example 2: Dependency flow

```text
Request → Interface → Use Case → Entity → Response
```

### Example 3: Avoid circular dependencies

```python
# retrieval.py (independent module)
def retrieve(query: str) -> list:
    return ["document1", "document2"]


# service.py (uses retrieval)
def answer_question(question: str) -> dict:
    docs = retrieve(question)
    return {"answer": "Response", "docs": docs}
```

**Why this is useful:**
Clean architecture makes it easier to test, replace parts, and understand the flow.

## 7. Design patterns

### Example 1: Factory pattern

```python
class ModelServiceFactory:
    @staticmethod
    def create(model_type: str):
        if model_type == "openai":
            return OpenAIService()
        elif model_type == "local":
            return LocalModelService()
        else:
            raise ValueError(f"Unknown model type: {model_type}")


class OpenAIService:
    def generate_answer(self, question):
        return "OpenAI answer"


class LocalModelService:
    def generate_answer(self, question):
        return "Local answer"


service = ModelServiceFactory.create("local")
print(service.generate_answer("What is Python?"))
```

### Example 2: Observer pattern

```python
class EventBus:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def publish(self, event):
        for callback in self.subscribers:
            callback(event)


bus = EventBus()
bus.subscribe(lambda e: print(f"Event logged: {e}"))
bus.publish("Request received")
```

### Example 3: Singleton pattern

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.environment = "production"
        return cls._instance


config1 = Config()
config2 = Config()
print(config1 is config2)
```

## 8. Dependency injection

Dependency injection passes dependencies to a class instead of having it create them.

### Example 1: Constructor injection

```python
class AnswerService:
    def __init__(self, retriever, model):
        self.retriever = retriever
        self.model = model

    def answer(self, question):
        docs = self.retriever.retrieve(question)
        return self.model.generate(question, docs)


class Retriever:
    def retrieve(self, query):
        return ["doc1"]


class Model:
    def generate(self, question, docs):
        return "Answer"


retriever = Retriever()
model = Model()
service = AnswerService(retriever, model)
```

**Why this is useful:**
Dependencies are visible, testable, and easy to replace.

### Example 2: Interface-based injection

```python
from abc import ABC, abstractmethod


class DocumentRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str) -> list:
        pass


class Service:
    def __init__(self, retriever: DocumentRetriever):
        self.retriever = retriever

    def process(self, question: str):
        return self.retriever.retrieve(question)
```

### Example 3: Dependency container

```python
class Container:
    def __init__(self):
        self.services = {}

    def register(self, name: str, service):
        self.services[name] = service

    def get(self, name: str):
        return self.services[name]


container = Container()
container.register("retriever", Retriever())
container.register("model", Model())

retriever = container.get("retriever")
```

## 9. Asynchronous Python

Async allows a program to do multiple things concurrently.

### Example 1: Basic async function

```python
import asyncio


async def fetch_answer(question: str) -> str:
    await asyncio.sleep(1)  # Simulate I/O
    return "Python is useful"


async def main():
    result = await fetch_answer("What is Python?")
    print(result)


asyncio.run(main())
```

**Why this is useful:**
Async avoids blocking while waiting for I/O, making programs more responsive.

### Example 2: Concurrent tasks

```python
async def fetch_from_service(service: str):
    await asyncio.sleep(0.5)
    return f"Result from {service}"


async def main():
    results = await asyncio.gather(
        fetch_from_service("service1"),
        fetch_from_service("service2"),
        fetch_from_service("service3"),
    )
    print(results)


asyncio.run(main())
```

### Example 3: Timeout handling

```python
async def slow_operation():
    await asyncio.sleep(5)


async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=1.0)
    except asyncio.TimeoutError:
        print("Operation timed out")


asyncio.run(main())
```

### Common mistakes

#### Correct code
```python
async def fetch():
    await asyncio.sleep(1)
    return "done"


asyncio.run(fetch())
```

#### Wrong code
```python
async def fetch():
    await asyncio.sleep(1)
    return "done"


fetch()
```

#### Error
```text
RuntimeError: no running event loop
```

#### Why it happens

Async functions must be run with `asyncio.run()`, not called directly.

#### Fix

Use `asyncio.run()` to execute async functions.

## 10. Performance optimization

### Example 1: Profile code execution

```python
import time


def slow_function():
    start = time.perf_counter()
    result = sum(i for i in range(1000000))
    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed:.4f} seconds")
    return result


slow_function()
```

**Why this is useful:**
Profiling identifies bottlenecks before optimization.

### Example 2: Use appropriate data structures

```python
# Slow: searching a list
documents = ["doc1", "doc2", "doc3"]
if "doc2" in documents:
    print("Found")  # O(n)

# Fast: searching a set
documents_set = {"doc1", "doc2", "doc3"}
if "doc2" in documents_set:
    print("Found")  # O(1)
```

### Example 3: Cache expensive results

```python
from functools import lru_cache


@lru_cache(maxsize=128)
def expensive_calculation(n: int) -> int:
    return sum(i for i in range(n))


print(expensive_calculation(1000))
print(expensive_calculation(1000))  # Uses cache
```

## 11. Testing advanced code

### Example 1: Test with mocks

```python
from unittest.mock import Mock


class AnswerService:
    def __init__(self, retriever):
        self.retriever = retriever

    def answer(self, question):
        docs = self.retriever.retrieve(question)
        return f"Answer based on {docs}"


def test_answer_uses_retriever():
    mock_retriever = Mock()
    mock_retriever.retrieve.return_value = ["doc1"]

    service = AnswerService(mock_retriever)
    result = service.answer("Question")

    mock_retriever.retrieve.assert_called_once()
    assert "doc1" in result
```

### Example 2: Test abstract classes

```python
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass


class EmailValidator(Validator):
    def validate(self, value):
        return "@" in value


def test_email_validator():
    validator = EmailValidator()
    assert validator.validate("test@example.com")
    assert not validator.validate("invalid")
```

## Practice tasks

1. Design a class hierarchy for different types of LLM services.
2. Build an abstract `Retriever` class and implement multiple backends.
3. Write a decorator that measures function execution time.
4. Create a context manager for managing API connections.
5. Add comprehensive type hints to a service module.
6. Implement the factory pattern for creating model instances.
7. Use dependency injection to pass a retriever to a service.
8. Write async functions to fetch from multiple data sources concurrently.
9. Profile and optimize a slow Python function.
10. Test a class with mocked dependencies.

## Quick debugging tips

- Use type checkers like `mypy` to catch type annotation errors early.
- Use `abc.abstractmethod` to enforce implementation of required methods.
- Keep decorators simple; test them separately.
- Use `with` statements for all resource management.
- Profile before optimizing; measure improvement after.
- Mock external dependencies in tests.
- Avoid circular imports by respecting layer boundaries.
- Use async when dealing with I/O, not CPU-bound work.

This module brings professional engineering practices to Python applications, enabling teams to build, maintain, and extend complex systems safely.
