# 04 - AI Agents and LLM Workflows

An AI agent is a program that can take a task, reason about it, call tools or services, and produce a result. A large language model (LLM) is a model trained on text that can generate responses, summarize text, classify content, or help with code.

This module explains the basics using simple Python examples.

## 1. What is an AI agent?

### Example 1: A simple decision agent

```python
# A very simple agent decides based on a user request.
user_request = "Write a summary of the meeting notes"

if "summary" in user_request.lower():
    action = "summarize_text"
elif "email" in user_request.lower():
    action = "draft_email"
else:
    action = "answer_question"

print(f"Agent action: {action}")
```

**Why this is useful:**
A basic agent chooses a tool or behavior based on the task.

### Example 2: Agent with a tool choice

```python
# A simple agent can choose between different tools.
user_task = "analyze support ticket"

tools = {
    "summarize": "summarize_text",
    "analyze": "classify_issue",
    "search": "lookup_ticket_history"
}

chosen = "analyze" if "analyze" in user_task.lower() else "summarize"
print(f"Chosen tool: {tools[chosen]}")
```

### Example 3: Agent loop

```python
# Agent loop: receive task, decide action, perform it, return result.
process = [
    "understand task",
    "choose tool",
    "run tool",
    "return answer"
]

for step in process:
    print(step)
```

### Common mistakes

#### Correct code
```python
user_task = "summarize report"
print(user_task.lower())
```

#### Wrong code
```python
user_task = "summarize report"
print(user_task.upper())
```

#### Error
```text
No syntax error, but the logic is wrong for this use case.
```

#### Why it happens

This is not a Python error, but it changes the task text. Lowercase may be needed for comparison, but uppercase may break exact matching if the system expects original strings.

#### Fix
```python
user_task = "summarize report"
normalized = user_task.lower()
print(normalized)
```

## 2. LLMs and prompt design

### Example 1: Simple prompt

```python
prompt = "Explain Python in 3 sentences for a beginner."
print(prompt)
```

**Why this is useful:**
An LLM needs a clear instruction to generate the correct output.

### Example 2: Structured prompt

```python
prompt = """
You are a coding tutor.
Explain what a variable is in Python.
Keep it to 4 bullet points.
"""

print(prompt)
```

### Example 3: System and user prompt separation

```python
system_prompt = "You are a helpful DevOps assistant."
user_prompt = "Explain what a deployment pipeline is."

print(f"System: {system_prompt}\nUser: {user_prompt}")
```

**Why this is useful:**
In real LLM apps, the system message sets the behavior, and the user message asks the task.

### Common mistakes

#### Correct code
```python
system_prompt = "You are a helpful assistant"
user_prompt = "Explain Python loops"
print(system_prompt)
print(user_prompt)
```

#### Wrong code
```python
system_prompt = "You are a helpful assistant"
user_prompt = "Explain Python loops"
print(system_prompt + user_prompt)
```

#### Error
```text
This may not be an error, but the result is poor because the prompt is not structured clearly.
```

#### Why it happens

The system instruction and the user task are combined without separation. This can weaken the model's behavior.

#### Fix
```python
system_prompt = "You are a helpful assistant"
user_prompt = "Explain Python loops"
print(f"System: {system_prompt}\nUser: {user_prompt}")
```

## 3. Calling an LLM API with Python

### Example 1: Basic HTTP request to an LLM endpoint

```python
import requests

url = "https://example.com/llm-api"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
body = {"prompt": "Explain Python variables in simple words"}

response = requests.post(url, headers=headers, json=body)
print(response.status_code)
print(response.text)
```

**Why this is useful:**
This is the general pattern used when connecting Python to any AI service.

### Example 2: Using environment variables

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
print("API key loaded:", bool(api_key))
```

**Why this is useful:**
Never hardcode secrets in source files. Use environment variables.

### Example 3: A function to send a prompt

```python
import os
import requests

def call_llm(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"prompt": prompt}
    response = requests.post("https://example.com/llm-api", headers=headers, json=payload)
    return response.json()

print(call_llm("Explain Python loops in 2 sentences"))
```

### Common mistakes

#### Correct code
```python
import os
api_key = os.getenv("OPENAI_API_KEY")
print(api_key is not None)
```

#### Wrong code
```python
api_key = "YOUR_SECRET_KEY"
print(api_key)
```

#### Error
```text
No error, but this is a security issue.
```

#### Why it happens

Hardcoded API keys can leak into version control and public repositories.

#### Fix
```python
import os
api_key = os.getenv("OPENAI_API_KEY")
```

## 4. A simple agent function call

### Example 1: Tool selection agent

```python
def choose_tool(task):
    task_lower = task.lower()
    if "email" in task_lower:
        return "draft_email"
    if "summary" in task_lower:
        return "summarize_text"
    return "answer_question"

print(choose_tool("Write a summary of this document"))
```

### Example 2: Agent with memory

```python
memory = []

def agent(task):
    memory.append(task)
    return f"Handled: {task}"

print(agent("Create a travel plan"))
print(memory)
```

### Example 3: Agent that calls a tool

```python
def summarize_text(text):
    return f"Summary: {text[:40]}..."

def agent(task, text):
    if "summary" in task.lower():
        return summarize_text(text)
    return "No summary requested"

print(agent("summary this article", "Python is easy to learn and useful for automation."))
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

The function requires two arguments, but only one is passed.

#### Fix
```python
def add(a, b):
    return a + b

print(add(2, 3))
```

## 5. RAG: Retrieval-Augmented Generation

RAG means the model looks up relevant documents or data before answering.

### Example 1: Basic knowledge lookup

```python
knowledge_base = {
    "python": "Python is a high-level programming language used for automation and AI.",
    "devops": "DevOps combines software development and IT operations.",
    "llm": "LLMs generate text by predicting the next token from input context."
}

query = "python"
print(knowledge_base.get(query, "No match found"))
```

### Example 2: Search by keyword

```python
docs = [
    "Python is good for scripts and automation.",
    "Docker helps package applications.",
    "LLMs use prompts to generate content."
]

query = "python"
for doc in docs:
    if query.lower() in doc.lower():
        print(doc)
```

### Example 3: Document retrieval idea

```python
# A simple retrieval step.
user_question = "What is Python used for?"
relevant_docs = [
    "Python is used for automation, web apps, and ML.",
    "Java is used for enterprise backend services."
]

for doc in relevant_docs:
    if "Python" in doc:
        print(doc)
```

**Why this is useful:**
RAG gives the model relevant facts before it answers a question.

## 6. LLM use cases in real work

### Example 1: Customer support summarization

```python
support_ticket = "Customer says login is slow and they cannot access the dashboard."
print(f"Ticket summary: {support_ticket}")
```

### Example 2: Code review assistant

```python
code_snippet = "def add(a, b): return a + b"
print(f"Review suggestion: Check function naming and test coverage for {code_snippet}")
```

### Example 3: AI onboarding assistant

```python
employee_question = "How do I deploy a new service?"
print(f"Suggested answer: Read the deployment guide and validate with staging checks.")
```

## 7. Agentic AI workflow

### Example 1: Plan → tool → answer

```python
steps = [
    "Understand the user request",
    "Select the right tool",
    "Run the tool",
    "Return the final answer"
]

for step in steps:
    print(step)
```

### Example 2: Tool-call pattern

```python
def run_tool(tool_name, input_data):
    if tool_name == "summarize_text":
        return f"Summary of {input_data}: Key points extracted."
    if tool_name == "search_docs":
        return f"Results for {input_data}: 3 relevant articles found."
    return "Tool not found"

print(run_tool("summarize_text", "meeting notes"))
```

### Example 3: Agent with validation

```python
def validate_answer(answer):
    return len(answer) > 5

answer = "This is okay"
print(validate_answer(answer))
```

**Why this is useful:**
A good agent validates its output before returning it.

## Practice tasks

1. Write a small script that chooses a tool based on the task text.
2. Write a function that builds a prompt with system and user roles.
3. Simulate a simple RAG workflow with 3 documents and a user question.
4. Create a script that reads a question from the command line and prints a simple LLM-style response template.
5. Build a fake agent that decides between `summarize`, `search`, and `answer` actions.

## Quick debugging tips

- Check if your API key is loaded correctly before making requests.
- Print the request payload before sending it to the model.
- Keep prompts short, clear, and specific.
- Validate output after the model responds.
- Use environment variables for secrets and configuration.
- If retrieval is poor, improve the search keywords or document quality.

This topic builds the bridge between Python basics and real-world AI products, agents, and intelligent workflows.
