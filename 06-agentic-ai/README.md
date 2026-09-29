# 06 - Agentic AI

Agentic AI is a style of AI where the system is not only answering a prompt, but also planning, choosing tools, making decisions, and executing a sequence of steps to complete a task.

Unlike a simple chatbot that answers a single question, an agent can behave more like a task runner. It may read information, decide a plan, call tools, check results, and improve its next step.

## 1. What is an agent?

### Example 1: A simple planning agent

```python
# A simple agent decides what to do next.
user_task = "Create a daily report"

plan = [
    "collect data",
    "format results",
    "write report",
    "save final output"
]

print(f"Task: {user_task}")
for step in plan:
    print(f"- {step}")
```

**Why this is useful:**
Agents work by dividing tasks into steps rather than trying to do everything in one action.

### Example 2: Agent with task selection

```python
# A basic agent decides the next action based on the request.
request = "summarize customer feedback"

if "summary" in request.lower():
    action = "summarize_text"
elif "search" in request.lower():
    action = "search_docs"
else:
    action = "answer_question"

print(f"Chosen action: {action}")
```

### Example 3: Agent loop

```python
# A simple loop that simulates an agent workflow.
for step in ["receive task", "choose tool", "execute step", "evaluate result"]:
    print(step)
```

### Common mistakes

#### Correct code
```python
request = "summarize customer feedback"
print(request.lower())
```

#### Wrong code
```python
request = "summarize customer feedback"
print(request[0])
```

#### Error
```text
This may not be an error, but it is not the correct logic.
```

#### Why it happens

The code prints only the first character instead of the full request. For an agent, we usually need the whole task text for matching and routing.

#### Fix
```python
request = "summarize customer feedback"
print(request.lower())
```

## 2. Memory and context in agents

### Example 1: A memory list

```python
conversation_memory = []

conversation_memory.append("User asked for a summary")
conversation_memory.append("Agent used a summarization tool")

print(conversation_memory)
```

**Why this is useful:**
Agents often keep memory of previous steps so they can continue a task consistently.

### Example 2: Simple short-term memory

```python
memory = {"last_task": "draft email", "status": "completed"}
print(memory)
```

### Example 3: Using memory to guide the next action

```python
memory = {"last_action": "search_docs"}

if memory.get("last_action") == "search_docs":
    print("Next step: summarize the search results")
else:
    print("Next step: choose a tool")
```

### Common mistakes

#### Correct code
```python
memory = {"last_action": "search_docs"}
print(memory.get("last_action"))
```

#### Wrong code
```python
memory = {"last_action": "search_docs"}
print(memory["Last_Action"])
```

#### Error
```text
KeyError: 'Last_Action'
```

#### Why it happens

Dictionary keys are case-sensitive. `"last_action"` is not the same as `"Last_Action"`.

#### Fix
```python
memory = {"last_action": "search_docs"}
print(memory["last_action"])
```

## 3. Tool calling pattern

### Example 1: Tool selection function

```python
def choose_tool(task):
    task_lower = task.lower()
    if "email" in task_lower:
        return "draft_email"
    if "summary" in task_lower:
        return "summarize_text"
    return "answer_question"

print(choose_tool("write a summary of the notes"))
```

### Example 2: Calling a tool

```python
def summarize_text(text):
    return f"Summary: {text[:40]}..."

result = summarize_text("This is a long meeting note and the summary should be concise.")
print(result)
```

### Example 3: Simple agent tool pipeline

```python
def search_docs(query):
    return f"Search results for: {query}"

def summarize_text(text):
    return f"Summary: {text}"

query = "python automation"
search_result = search_docs(query)
print(search_result)
print(summarize_text(search_result))
```

### Common mistakes

#### Correct code
```python
def summarize_text(text):
    return f"Summary: {text}"

print(summarize_text("python automation"))
```

#### Wrong code
```python
def summarize_text(text):
    return f"Summary: {text}"

print(summarize_text())
```

#### Error
```text
TypeError: summarize_text() missing 1 required positional argument: 'text'
```

#### Why it happens

The function requires one argument, but none was passed.

#### Fix
```python
def summarize_text(text):
    return f"Summary: {text}"

print(summarize_text("python automation"))
```

## 4. Planning before action

### Example 1: Plan generation

```python
# A simple plan for an agent.
plan = [
    "understand user request",
    "collect necessary data",
    "decide approach",
    "execute action",
    "validate output"
]

for step in plan:
    print(step)
```

### Example 2: Conditional planning

```python
need_research = True

if need_research:
    print("Plan: gather facts first")
else:
    print("Plan: answer directly")
```

### Example 3: Multi-step workflow

```python
workflow = {
    "step_1": "read task",
    "step_2": "find relevant data",
    "step_3": "generate answer",
    "step_4": "check quality"
}

for key, value in workflow.items():
    print(f"{key}: {value}")
```

## 5. Reasoning and validation loops

### Example 1: Validate output length

```python
def validate_answer(answer):
    return len(answer) > 10

answer = "This answer is long enough"
print(validate_answer(answer))
```

### Example 2: Retry pattern

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1
```

### Example 3: Final answer decision

```python
result_quality = "good"
if result_quality == "good":
    print("Return result to user")
else:
    print("Improve the result before returning")
```

**Why this is useful:**
Agents often repeat steps until the output is good enough.

## 6. Real-world agentic AI examples

### Example 1: Support agent

```python
# Simulated support agent workflow.
issue = "Customer cannot log in"
print(f"Agent finds issue: {issue}")
print("Agent checks credentials, password reset option, and login logs")
```

### Example 2: Research assistant

```python
# A research agent collects facts and writes a summary.
question = "What is Python used for?"
print(f"Research query: {question}")
print("Collect data, summarize, prepare answer")
```

### Example 3: DevOps agent

```python
# An automation agent checks deployment health.
status = "healthy"
if status == "healthy":
    print("Proceed with next deployment step")
else:
    print("Pause and investigate")
```

## 7. Agentic AI with LLMs

### Example 1: Prompting an agent

```python
prompt = "You are a helpful assistant. Read the customer request, decide the tool, and answer clearly."
print(prompt)
```

### Example 2: Tool-chain idea

```python
tools = ["web_search", "calculator", "database_lookup", "email_draft"]
for tool in tools:
    print(tool)
```

### Example 3: Human approval step

```python
approved = True
if approved:
    print("Proceed with final action")
else:
    print("Wait for user approval")
```

**Why this is useful:**
In real agent systems, a human may review high-risk actions before execution.

## Practice tasks

1. Write a Python function that chooses a tool based on a user request.
2. Build a simple agent memory dictionary that stores the last task and last action.
3. Write a small planning loop that prints the steps for a new task.
4. Create a fake support agent that responds to login and billing issues.
5. Build a simple validation function that checks whether an answer is long enough and relevant.

## Quick debugging tips

- Check if your task text matches the keywords you expect.
- Make sure dictionary keys match exactly.
- Print the selected tool before execution to debug the decision flow.
- Validate the output before sending it to the user.
- Keep memory data simple and easy to inspect.
- Use short, clear steps in the workflow so each action is easy to debug.

This topic is the bridge from simple AI usage to real agentic systems that can perform multi-step work.
