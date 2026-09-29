# 12 - Interview Preparation and Coding Challenges

This module prepares you for Python, AI/ML, LLM, agent, and software-engineering interviews. The goal is not to memorize answers. The goal is to explain your thinking, write correct code, test it, and make sensible engineering trade-offs.

## 1. A reliable interview workflow

Use this process for coding questions:

1. Restate the problem in your own words.
2. Ask about inputs, outputs, constraints, and edge cases.
3. Give a simple example.
4. Describe a straightforward solution.
5. Improve it if the constraints require better performance.
6. Write readable code.
7. Test normal, boundary, and invalid cases.
8. State time and space complexity.

### Example: Two-sum problem

```python
def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return indexes of two values whose sum equals target."""
    seen: dict[int, int] = {}

    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return seen[needed], index
        seen[number] = index

    return None


print(two_sum([2, 7, 11, 15], 9))
```

**Reasoning:** Store values already visited in a dictionary. Each new value checks whether its complement has appeared.

**Complexity:** `O(n)` time and `O(n)` additional space.

### Common mistake

```python
# This can raise IndexError when the list is empty.
first = numbers[0]
```

Check assumptions before indexing, and always discuss empty input during an interview.

## 2. Big-O complexity

Big-O describes how resource usage grows as input size increases.

| Pattern | Typical complexity | Example |
|---|---:|---|
| Constant lookup | `O(1)` average | dictionary key lookup |
| One loop | `O(n)` | scan a list |
| Nested loops | `O(n²)` | compare every pair |
| Binary search | `O(log n)` | search sorted data |
| Sorting | `O(n log n)` | `sorted(values)` |

### Example: Compare approaches

```python
def has_duplicate_slow(values: list[int]) -> bool:
    for index, value in enumerate(values):
        if value in values[index + 1:]:
            return True
    return False


def has_duplicate_fast(values: list[int]) -> bool:
    return len(values) != len(set(values))
```

The first approach can take `O(n²)` time. The set-based approach typically takes `O(n)` time and `O(n)` space.

### Complexity checklist

- Count loops and nested loops.
- Include sorting costs.
- Include memory used by lists, sets, dictionaries, and recursion.
- Mention average-case assumptions for hash tables.
- Do not optimize before understanding the constraints.

## 3. Core data structures

### Lists

Use lists for ordered, indexable collections.

```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers[0])
```

### Sets

Use sets for membership checks and uniqueness.

```python
unique_words = set(["ai", "python", "ai"])
print(unique_words)
```

### Dictionaries

Use dictionaries to map keys to values or count items.

```python
from collections import Counter

counts = Counter("banana")
print(counts["a"])
```

### Queues and stacks

```python
from collections import deque

queue = deque(["first"])
queue.append("second")
print(queue.popleft())

stack = []
stack.append("page-1")
print(stack.pop())
```

### Heaps

```python
import heapq

priorities = [5, 1, 3]
heapq.heapify(priorities)
print(heapq.heappop(priorities))
```

Use a heap for repeatedly selecting the smallest or highest-priority item.

## 4. Common coding patterns

### Sliding window

Useful for contiguous ranges.

```python
def max_sum_window(values: list[int], window_size: int) -> int:
    if window_size <= 0 or window_size > len(values):
        raise ValueError("Invalid window size")

    current = sum(values[:window_size])
    best = current

    for index in range(window_size, len(values)):
        current += values[index] - values[index - window_size]
        best = max(best, current)

    return best


print(max_sum_window([2, 1, 5, 1, 3, 2], 3))
```

### Two pointers

Useful for sorted arrays and palindrome checks.

```python
def is_palindrome(text: str) -> bool:
    left, right = 0, len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True
```

### Binary search

```python
def binary_search(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

The input must be sorted for this implementation to be correct.

### Breadth-first search

```python
from collections import deque


def shortest_steps(graph: dict[str, list[str]], start: str, goal: str) -> int | None:
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, distance = queue.popleft()
        if node == goal:
            return distance

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))

    return None
```

### Recursion and backtracking

Use recursion when a problem naturally contains smaller versions of itself, such as tree traversal or generating combinations.

```python
def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)
```

Always identify the base case and consider recursion-depth limits.

## 5. Python interview questions

### What is the difference between a list and a tuple?

A list is mutable; a tuple is immutable. Use a tuple for fixed records or values that should not change.

```python
mutable_values = [1, 2]
fixed_values = (1, 2)
mutable_values.append(3)
```

### What is the difference between `is` and `==`?

`==` compares values. `is` checks object identity. Use `is None` when checking for `None`.

```python
value = None
if value is None:
    print("No value")
```

### Why use a virtual environment?

It isolates project dependencies so one project cannot unexpectedly break another.

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate          # Windows
python -m pip install --upgrade pip
```

### What is a generator?

A generator produces values lazily, which can reduce memory usage.

```python
def count_up_to(limit: int):
    for number in range(limit):
        yield number

for number in count_up_to(3):
    print(number)
```

### What is a context manager?

It controls setup and cleanup around a block, commonly for files, locks, and database connections.

```python
with open("notes.txt", encoding="utf-8") as file:
    text = file.read()
```

## 6. Testing and debugging under pressure

### Example: Test-driven thinking

```python
def normalize_email(email: str) -> str:
    return email.strip().lower()


def test_normalize_email():
    assert normalize_email("  User@Example.COM ") == "user@example.com"
    assert normalize_email("") == ""
```

### Debugging checklist

- Reproduce the failure with the smallest input.
- Read the exception type and traceback from the bottom upward.
- Print or inspect intermediate values.
- Check types, indexes, and boundary conditions.
- Add a focused test for the bug.
- Fix the cause rather than hiding the exception.

### Exception handling

```python
def parse_age(value: str) -> int:
    try:
        age = int(value)
    except ValueError as error:
        raise ValueError("Age must be a whole number") from error

    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

Avoid a bare `except:` because it also catches interrupts and unexpected system exceptions.

## 7. AI and ML interview fundamentals

Be ready to explain:

- supervised, unsupervised, and reinforcement learning;
- train, validation, and test splits;
- overfitting and underfitting;
- precision, recall, F1, ROC-AUC, and confusion matrices;
- data leakage and class imbalance;
- feature engineering and preprocessing;
- model versioning and reproducibility;
- offline evaluation versus production monitoring;
- fairness, privacy, and human review.

### Example: Precision and recall

```python
def precision(true_positive: int, false_positive: int) -> float:
    total = true_positive + false_positive
    return true_positive / total if total else 0.0


def recall(true_positive: int, false_negative: int) -> float:
    total = true_positive + false_negative
    return true_positive / total if total else 0.0
```

Explain the business impact: in medical screening, missing a positive case may be more serious than reviewing extra false positives.

## 8. LLM and RAG interview questions

### What is a token?

A token is a unit used by a language model to represent text. Token counts affect context limits, latency, and cost.

### What is RAG?

Retrieval-augmented generation retrieves relevant external information and supplies it as context to a model. It can improve freshness and grounding without retraining the model.

A typical RAG flow is:

```text
Documents → chunking → embeddings → vector index
                                     ↓
Question → embedding → retrieval → prompt → model → cited answer
```

### What causes poor RAG answers?

- bad chunk size or overlap;
- weak embedding model;
- irrelevant retrieval;
- too many context documents;
- missing metadata filters;
- prompt instructions that do not require grounding;
- evaluation data that does not represent real questions.

### What is fine-tuning?

Fine-tuning updates model parameters using task-specific examples. It differs from RAG, which supplies information at inference time. Choose fine-tuning for behavior or format changes, and RAG for changing knowledge.

### How do you evaluate an LLM application?

Use a combination of:

- task accuracy or correctness;
- groundedness and citation checks;
- retrieval precision and recall;
- safety and refusal tests;
- latency and cost;
- human review;
- regression datasets;
- production feedback.

## 9. AI system-design interview

### Example: Design a document assistant

Start with requirements:

- Who are the users?
- What file types and data volumes are expected?
- Is the answer allowed to use only company documents?
- What are latency, cost, privacy, and availability targets?
- Which actions require approval?

Then describe the architecture:

```text
Client
  ↓
API gateway and authentication
  ↓
Request validation and rate limiting
  ↓
Query service ─── cache
  ↓
Retriever ─────── vector database + metadata store
  ↓
Prompt builder
  ↓
Model gateway ─── provider or local model
  ↓
Output validation and citations
  ↓
Response, metrics, traces, audit logs
```

Discuss failure modes:

- provider timeout → bounded retry or fallback;
- no relevant documents → say that evidence was not found;
- prompt injection in a document → treat retrieved text as untrusted data;
- sensitive document → enforce authorization before retrieval;
- high cost → cache, route simple requests to a smaller model, and limit context;
- bad release → version and roll back prompts, code, indexes, and models.

## 10. Behavioral interviews

Use the **STAR** structure:

- **Situation:** What was happening?
- **Task:** What responsibility did you have?
- **Action:** What did you do and why?
- **Result:** What changed? Include measurable outcomes when possible.

Prepare examples for:

- fixing a production incident;
- disagreeing respectfully;
- learning an unfamiliar tool;
- reducing cost or latency;
- improving reliability;
- receiving critical feedback;
- explaining a technical idea to a non-technical person.

Do not claim that AI-generated code was your work without understanding, testing, and being able to explain it.

## 11. Practice challenge set

### Beginner

1. Reverse a string.
2. Count vowels in a sentence.
3. Find the largest number in a list without `max()`.
4. Remove duplicates while preserving order.
5. Count word frequencies.

### Intermediate

6. Find the first non-repeating character.
7. Merge overlapping intervals.
8. Implement a least-recently-used cache.
9. Find the shortest path in an unweighted graph.
10. Process a large log file without loading it all into memory.

### AI-focused

11. Implement keyword retrieval and return ranked documents.
12. Split a document into overlapping chunks.
13. Build a prompt with a maximum context length.
14. Calculate precision, recall, and F1 from predictions.
15. Add retry and timeout handling to a model client.
16. Design an evaluation dataset for a customer-support assistant.
17. Identify prompt-injection risks in a RAG pipeline.
18. Estimate cost from input and output token counts.

For each solution, provide:

- assumptions;
- a readable implementation;
- at least three tests;
- time and space complexity;
- one alternative approach;
- limitations and production considerations.

## 12. Practice environments and useful links

- Python documentation: https://docs.python.org/3/
- Python tutorial: https://docs.python.org/3/tutorial/
- pytest documentation: https://docs.pytest.org/
- Exercism Python track: https://exercism.org/tracks/python
- LeetCode: https://leetcode.com/
- HackerRank Python practice: https://www.hackerrank.com/domains/python
- Codewars: https://www.codewars.com/
- Kaggle learn: https://www.kaggle.com/learn
- Google Colab: https://colab.research.google.com/
- Jupyter: https://jupyter.org/
- Hugging Face tasks and models: https://huggingface.co/
- scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- OpenAI documentation: https://platform.openai.com/docs/
- Anthropic documentation: https://docs.anthropic.com/
- Google Gemini documentation: https://ai.google.dev/

Some platforms offer free practice; API providers and cloud services may charge for usage. Check current pricing before sending production data or enabling paid services.

## 13. Mock interview plan

### Round 1: Python fundamentals

- 20 minutes: explain data structures and Python behavior.
- 30 minutes: solve two easy coding problems.
- 10 minutes: test and discuss complexity.

### Round 2: Algorithms

- 10 minutes: clarify constraints.
- 35 minutes: solve one medium problem.
- 15 minutes: improve and test the solution.

### Round 3: AI application design

- 10 minutes: requirements.
- 20 minutes: architecture and data flow.
- 15 minutes: evaluation, security, cost, and failure handling.

### Round 4: Behavioral

Answer three STAR questions in concise, specific language.

## Final preparation checklist

- [ ] I can explain lists, sets, dictionaries, stacks, queues, and heaps.
- [ ] I can analyze time and space complexity.
- [ ] I can write tests before or alongside implementation.
- [ ] I can debug a traceback methodically.
- [ ] I can explain Python packaging and virtual environments.
- [ ] I can explain ML evaluation and data leakage.
- [ ] I can describe an LLM, RAG, and agent architecture.
- [ ] I can discuss security, privacy, cost, latency, and reliability.
- [ ] I have solved problems without copying solutions.
- [ ] I can explain every line of my portfolio projects.

The best preparation is deliberate practice: solve a problem, explain your trade-offs, test edge cases, review the solution, and repeat until the reasoning becomes clear and consistent.
