# 07 - LLM Project Patterns and Production Workflows

Large language models (LLMs) are powerful, but real projects need more than just a prompt. Production workflows include input validation, prompt design, retrieval, tool use, structured output, testing, and response safety.

This module explains how to design simple LLM-based projects in a realistic way.

## 1. Prompt template basics

### Example 1: A simple prompt template

```python
prompt_template = """
You are a helpful assistant.
Answer the user question clearly and briefly.
Question: {question}
"""

question = "What is Python used for?"
print(prompt_template.format(question=question))
```

**Why this is useful:**
Prompt templates help keep responses consistent and easier to test.

### Example 2: Prompt with context

```python
context = "Python is used for automation, scripting, AI, and web development."
question = "Why is Python popular for automation?"

prompt = f"Context: {context}\nQuestion: {question}\nAnswer with 2 bullet points."
print(prompt)
```

### Example 3: Prompt with role instructions

```python
system_role = "You are an expert software engineer."
user_question = "Explain what a loop is in Python."

prompt = f"{system_role}\nUser: {user_question}"
print(prompt)
```

### Common mistakes

#### Correct code
```python
name = "Asha"
print(f"Hello {name}")
```

#### Wrong code
```python
name = "Asha"
print("Hello {name}")
```

#### Error
```text
This may not cause a crash, but it prints the literal text instead of the value.
```

#### Why it happens

`f`-strings only evaluate expressions inside curly braces when the string starts with `f`.

#### Fix
```python
name = "Asha"
print(f"Hello {name}")
```

## 2. Structured outputs

### Example 1: Return JSON-like output

```python
result = {
    "status": "success",
    "summary": "Python is used for automation and AI.",
    "confidence": 0.95
}

print(result)
```

**Why this is useful:**
Structured outputs are easier for other applications to process.

### Example 2: Use a Python dictionary for a model result

```python
response = {
    "question": "What is DevOps?",
    "answer": "DevOps combines development and operations.",
    "category": "concept"
}

print(response["answer"])
```

### Example 3: Validate structure

```python
response = {
    "status": "ok",
    "answer": "Python is useful for automation."
}

if "status" in response and "answer" in response:
    print("Response has the expected structure")
else:
    print("Response is incomplete")
```

### Common mistakes

#### Correct code
```python
response = {"status": "ok"}
print(response.get("status"))
```

#### Wrong code
```python
response = {"status": "ok"}
print(response["Status"])
```

#### Error
```text
KeyError: 'Status'
```

#### Why it happens

Dictionary keys are case-sensitive.

#### Fix
```python
response = {"status": "ok"}
print(response["status"])
```

## 3. Retrieval workflow

### Example 1: Simple document lookup

```python
documents = {
    "python": "Python is used for automation and AI.",
    "docker": "Docker packages applications into containers.",
    "kubernetes": "Kubernetes orchestrates containerized workloads."
}

query = "python"
print(documents.get(query, "No matching document found"))
```

### Example 2: Search for matching document names

```python
documents = [
    "Python automation tutorial",
    "Docker basics",
    "Kubernetes deployment guide"
]

search_term = "python"
for doc in documents:
    if search_term.lower() in doc.lower():
        print(doc)
```

### Example 3: Simulated RAG flow

```python
context = [
    "Python is good for automation.",
    "Docker helps package applications.",
    "Kubernetes manages containers."
]

user_question = "What is Python good for?"

for paragraph in context:
    if "Python" in paragraph:
        print(f"Relevant context: {paragraph}")
```

## 4. Tool calling patterns

### Example 1: Tool router

```python
def route_tool(task):
    task_lower = task.lower()
    if "search" in task_lower:
        return "search_docs"
    if "calculate" in task_lower:
        return "calculator"
    return "answer_question"

print(route_tool("search for python docs"))
```

### Example 2: Tool result handling

```python
def calculator(number_a, number_b):
    return number_a + number_b

result = calculator(10, 5)
print(f"Result: {result}")
```

### Example 3: Agent-like tool selection

```python
request = "calculate monthly revenue"
selected_tool = "calculator" if "calculate" in request.lower() else "answer_question"
print(f"Selected tool: {selected_tool}")
```

### Common mistakes

#### Correct code
```python
def add(a, b):
    return a + b

print(add(2, 3))
```

#### Wrong code
```python
def add(a, b):
    return a + b

print(add(2))
```

#### Error
```text
TypeError: add() missing 1 required positional argument: 'b'
```

#### Why it happens

The function needs two arguments but only one was supplied.

#### Fix
```python
def add(a, b):
    return a + b

print(add(2, 3))
```

## 5. Guardrails and validation

### Example 1: Check answer length

```python
def answer_is_valid(answer):
    return len(answer) > 10

print(answer_is_valid("This is valid"))
```

### Example 2: Block unsafe content pattern

```python
text = "This is a normal answer"
if "ignore previous" in text.lower():
    print("Unsafe instruction detected")
else:
    print("Safe content")
```

### Example 3: Validate required fields

```python
response = {"answer": "Python is useful for automation."}
if "answer" in response:
    print("Required content present")
else:
    print("Required content missing")
```

**Why this is useful:**
Production AI systems must check that responses are valid and relevant.

## 6. Prompt safety and testing

### Example 1: Test a prompt

```python
prompt = "Explain Python in 2 sentences."
print(prompt)
```

### Example 2: Test with different inputs

```python
questions = [
    "What is Python?",
    "How does Python help with automation?",
    "Why use Python for AI?"
]

for question in questions:
    print(question)
```

### Example 3: Test for bad output shape

```python
response = {"status": "success"}
if "answer" not in response:
    print("Warning: response missing answer field")
```

## 7. Production workflow pattern

### Example 1: Request → retrieve → prompt → validate → return

```python
user_question = "What is Python used for?"
context = ["Python is used for automation, AI, and scripting."]
prompt = f"Question: {user_question}\nContext: {context[0]}"
print(prompt)
```

### Example 2: Add a quality gate

```python
answer = "Python is useful for automation and AI."
if len(answer) > 20:
    print("Quality gate passed")
else:
    print("Quality gate failed")
```

### Example 3: Human approval for risky tasks

```python
risky_action = True
if risky_action:
    print("Request human approval before final execution")
else:
    print("Proceed automatically")
```

## Practice tasks

1. Build a prompt template that includes a system role and a user question.
2. Create a dictionary-based response structure for an LLM answer.
3. Write a simple retrieval program that finds the matching document for a user question.
4. Build a tool router that chooses between `search_docs`, `answer_question`, and `calculator`.
5. Write a validation function that rejects empty or too-short answers.

## Quick debugging tips

- Check if the question or prompt is missing important context.
- Keep prompt strings clear and specific.
- Validate structure before using the output in another system.
- Use print statements to inspect tool routing decisions.
- Check retrieval results before generating the final answer.
- Always test outputs with multiple input variations.

This topic focuses on the production-side thinking required to build reliable LLM-based systems.
