# 09 - Production Deployment and MLOps

A prototype can work on one laptop, but a production AI application needs repeatable builds, safe configuration, monitoring, testing, and a plan for failures. MLOps combines machine learning practices with software engineering and operations.

## 1. Production readiness

### Example 1: Readiness checklist

```python
checks = {
    "tests_passing": True,
    "secrets_externalized": True,
    "health_check_available": True,
    "logging_configured": True,
    "rollback_plan_ready": True,
}

ready = all(checks.values())
print("Ready for production" if ready else "Not ready for production")
```

**Why this is useful:**
A checklist turns important operational expectations into visible checks.

### Example 2: Required configuration

```python
import os

required = ["ENVIRONMENT", "MODEL_NAME"]
missing = [name for name in required if not os.getenv(name)]

if missing:
    raise RuntimeError(f"Missing configuration: {', '.join(missing)}")

print("Configuration is complete")
```

### Example 3: Health status

```python
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

print(health_check())
```

### Common mistakes

#### Correct code
```python
if all(checks.values()):
    print("All checks passed")
```

#### Wrong code
```python
if checks.values():
    print("All checks passed")
```

#### Error
```text
No syntax error, but the condition is misleading.
```

#### Why it happens

`checks.values()` returns a view object, not a check that every value is `True`.

#### Fix
```python
if all(checks.values()):
    print("All checks passed")
```

## 2. Dockerizing a Python application

Docker packages an application and its dependencies into a repeatable container image.

### Example 1: Basic Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "main.py"]
```

**Why this is useful:**
The same image can be tested in CI and deployed to different environments.

### Example 2: Requirements file

```text
# requirements.txt
fastapi
uvicorn
python-dotenv
```

### Example 3: Build and run commands

```bash
docker build -t ai-app:1.0.0 .
docker run --rm -p 8000:8000 ai-app:1.0.0
```

### Common mistakes

#### Correct code
```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

#### Wrong code
```dockerfile
RUN pip install -r requirements.txt
COPY requirements.txt .
```

#### Error
```text
ERROR: Could not open requirements file
```

#### Why it happens

The install command runs before the file has been copied into the image.

#### Fix

Copy files before commands that use them.

## 3. CI/CD pipeline design

Continuous integration runs checks for every change. Continuous delivery or deployment promotes validated changes through environments.

### Example 1: Pipeline stages

```python
stages = ["lint", "test", "build", "security_scan", "deploy"]

for stage in stages:
    print(f"Running stage: {stage}")
```

### Example 2: Stop after a failed stage

```python
results = {
    "lint": True,
    "test": True,
    "security_scan": False,
}

for stage, passed in results.items():
    print(f"{stage}: {'passed' if passed else 'failed'}")
    if not passed:
        print("Pipeline stopped")
        break
```

### Example 3: GitHub Actions workflow shape

```yaml
name: Python checks

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

### Common mistakes

#### Correct code
```yaml
- run: pip install -r requirements.txt
- run: pytest
```

#### Wrong code
```yaml
- run: pytest
- run: pip install -r requirements.txt
```

#### Error
```text
ModuleNotFoundError: No module named 'pytest'
```

#### Why it happens

Tests run before the project dependencies have been installed.

#### Fix

Install dependencies before running tests.

## 4. Environment management

Development, staging, and production should use separate configuration values.

### Example 1: Select an environment

```python
import os

environment = os.getenv("ENVIRONMENT", "development")

if environment == "production":
    print("Use production-safe settings")
else:
    print(f"Running in {environment}")
```

### Example 2: Environment-specific model settings

```python
settings = {
    "development": {"model": "small-model", "log_level": "DEBUG"},
    "production": {"model": "stable-model", "log_level": "INFO"},
}

selected = settings.get("production", settings["development"])
print(selected)
```

### Example 3: Never print secrets

```python
import os

api_key = os.getenv("LLM_API_KEY")
print("API key configured:", bool(api_key))
```

**Why this is useful:**
A program can confirm that a secret exists without exposing its value.

## 5. Versioning models and applications

Versioning makes it possible to identify what code, prompt, and model produced a result.

### Example 1: Application version

```python
APP_VERSION = "1.4.0"
print(f"Application version: {APP_VERSION}")
```

### Example 2: Model metadata

```python
model_info = {
    "name": "example-model",
    "version": "2026-01",
    "prompt_version": "v3",
}

print(model_info)
```

### Example 3: Include versions in a response

```python
response = {
    "answer": "Python supports automation.",
    "app_version": "1.4.0",
    "model_version": "2026-01",
}

print(response)
```

### Common mistakes

#### Correct code
```python
response = {"answer": "Done", "model_version": "v2"}
```

#### Wrong code
```python
response = {"answer": "Done"}
```

#### Why it is a problem

Without version metadata, reproducing or debugging a previous answer is harder.

#### Fix

Record application, model, and prompt versions where appropriate.

## 6. Logging and monitoring

Logs explain what happened. Metrics show how often and how well it happened.

### Example 1: Structured logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai_app")

logger.info("Request received", extra={"request_id": "abc-123"})
```

### Example 2: Measure a request

```python
import time

started = time.perf_counter()
# Simulated model work
answer = "Generated answer"
elapsed = time.perf_counter() - started

print({"answer": answer, "latency_seconds": round(elapsed, 4)})
```

### Example 3: Count failures

```python
requests_total = 10
failures_total = 2
error_rate = failures_total / requests_total
print(f"Error rate: {error_rate:.0%}")
```

### Common mistakes

#### Correct code
```python
requests_total = 10
failures_total = 2
error_rate = failures_total / requests_total
```

#### Wrong code
```python
requests_total = 0
failures_total = 2
error_rate = failures_total / requests_total
```

#### Error
```text
ZeroDivisionError: division by zero
```

#### Why it happens

There are no requests in the denominator.

#### Fix
```python
error_rate = failures_total / requests_total if requests_total else 0
```

## 7. Health checks and graceful failure

### Example 1: Dependency health

```python
def check_model_service(model_available):
    return {"model": "up" if model_available else "down"}

print(check_model_service(True))
```

### Example 2: Timeout handling

```python
def call_external_service():
    raise TimeoutError("Service took too long")

try:
    call_external_service()
except TimeoutError:
    print("Return a temporary failure and retry later")
```

### Example 3: Retry with a limit

```python
max_retries = 3
for attempt in range(1, max_retries + 1):
    print(f"Attempt {attempt}")
```

**Why this is useful:**
Retries can handle temporary failures, but a limit prevents endless loops.

## 8. Deployment strategies

### Example 1: Rolling deployment

```python
instances = ["app-1", "app-2", "app-3"]
for instance in instances:
    print(f"Update {instance}, check health, continue")
```

### Example 2: Blue-green deployment

```python
active_environment = "blue"
new_environment = "green"

print(f"Test {new_environment} before switching traffic from {active_environment}")
```

### Example 3: Canary deployment

```python
traffic_percentage = 10
print(f"Send {traffic_percentage}% of traffic to the new version")
```

## 9. Rollbacks and incident response

### Example 1: Rollback decision

```python
error_rate = 0.12
threshold = 0.05

if error_rate > threshold:
    print("Rollback deployment")
else:
    print("Continue monitoring")
```

### Example 2: Store a previous version

```python
current_version = "1.5.0"
previous_version = "1.4.0"

print(f"Current: {current_version}; rollback target: {previous_version}")
```

### Example 3: Incident checklist

```python
incident_steps = [
    "confirm the alert",
    "limit customer impact",
    "identify the latest change",
    "rollback or fix",
    "document the incident",
]

for step in incident_steps:
    print(step)
```

## 10. Security for production AI applications

### Example 1: Validate file type

```python
allowed_extensions = {".txt", ".md", ".pdf"}
filename = "notes.md"

from pathlib import Path
suffix = Path(filename).suffix.lower()
print("Allowed" if suffix in allowed_extensions else "Rejected")
```

### Example 2: Limit request size

```python
def accept_request(text, maximum_characters=5000):
    if len(text) > maximum_characters:
        raise ValueError("Request is too large")
    return True

print(accept_request("Short request"))
```

### Example 3: Avoid sensitive logs

```python
user_email = "user@example.com"
print({"event": "request_received", "user": "redacted"})
```

**Why this is useful:**
Production systems should minimize exposure of secrets and personal information.

## Practice project

Build a deployment-ready AI service simulation that:

1. Reads environment configuration.
2. Validates a question.
3. Retrieves context from local documents.
4. Generates a simulated response.
5. Records application and model versions.
6. Measures request latency.
7. Exposes a health-check function.
8. Handles timeouts with limited retries.
9. Runs tests in a CI pipeline.
10. Uses a rollback decision based on error rate.

## Quick debugging tips

- Reproduce the problem with the same application, model, and prompt versions.
- Check health endpoints before investigating the model itself.
- Separate transient failures from permanent configuration errors.
- Do not retry invalid input or authentication failures blindly.
- Inspect CI logs from the first failing step.
- Use correlation or request IDs to follow one request across services.
- Keep rollback instructions documented and tested.

This module completes the move from local AI experiments to production-minded deployment and MLOps.
