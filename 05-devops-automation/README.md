# 05 - DevOps Automation

DevOps is the practice of combining software development and IT operations so that code can be built, tested, deployed, and monitored reliably and quickly.

Python is widely used in DevOps for automation, configuration, deployment scripts, orchestration, monitoring, and infrastructure tasks.

## 1. What is DevOps?

### Example 1: Deployment flow

```python
# A simple representation of a deployment flow.
steps = [
    "Build code",
    "Run tests",
    "Package the app",
    "Deploy to staging",
    "Validate health checks",
    "Deploy to production"
]

for step in steps:
    print(step)
```

**Why this is useful:**
DevOps teams automate the full delivery flow so that changes move quickly and safely.

### Example 2: Monitoring a service

```python
# Simple status check for a service.
service_status = "healthy"

if service_status == "healthy":
    print("Service is running normally")
else:
    print("Service is degraded")
```

### Example 3: Basic release checklist

```python
checklist = {
    "build_passed": True,
    "tests_passed": True,
    "security_scan_passed": False,
    "deployment_ready": False
}

for item, value in checklist.items():
    print(f"{item}: {value}")
```

### Common mistakes

#### Correct code
```python
service_status = "healthy"
if service_status == "healthy":
    print("Service is running normally")
```

#### Wrong code
```python
service_status = "healthy"
if service_status = "healthy":
    print("Service is running normally")
```

#### Error
```text
SyntaxError: invalid syntax
```

#### Why it happens

`=` assigns a value. `==` compares values.

#### Fix
```python
service_status = "healthy"
if service_status == "healthy":
    print("Service is running normally")
```

## 2. Automation with Python

### Example 1: Create a deployment note

```python
# Generate a release note automatically.
release_note = "Build 1.2.3 deployed successfully"
with open("release_note.txt", "w") as file:
    file.write(release_note)
print("Release note created")
```

**Why this is useful:**
Teams often auto-generate logs and release notes during deployment.

### Example 2: Check a folder before deployment

```python
from pathlib import Path

release_dir = Path("releases")
if release_dir.exists():
    print("Release directory found")
else:
    print("Release directory missing")
```

### Example 3: Read environment values

```python
import os

env = os.getenv("ENVIRONMENT", "development")
print(f"Current environment: {env}")
```

**Why this is useful:**
Automation scripts often check the environment before running deployment logic.

### Common mistakes

#### Correct code
```python
import os
print(os.getenv("ENVIRONMENT", "development"))
```

#### Wrong code
```python
import os
print(os.getenv("ENVIRONMENT"))
```

#### Error
```text
No syntax error, but it returns None if the variable is not set.
```

#### Why it happens

`getenv()` returns `None` when the environment variable is missing unless you provide a default value.

#### Fix
```python
import os
print(os.getenv("ENVIRONMENT", "development"))
```

## 3. File automation in DevOps

### Example 1: Read a config file

```python
with open("config.ini", "r") as file:
    for line in file:
        print(line.strip())
```

**Why this is useful:**
Many DevOps scripts read configuration files for ports, app names, or environment settings.

### Example 2: Write a deployment log

```python
with open("deployment.log", "a") as file:
    file.write("Deployment started\n")
    file.write("Deployment finished\n")
print("Log written")
```

### Example 3: Count log lines

```python
with open("deployment.log", "r") as file:
    lines = file.readlines()
    print(f"Total log lines: {len(lines)}")
```

### Common mistakes

#### Correct code
```python
with open("deployment.log", "a") as file:
    file.write("Deployment started\n")
```

#### Wrong code
```python
with open("deployment.log", "r") as file:
    file.write("Deployment started\n")
```

#### Error
```text
io.UnsupportedOperation: not writable
```

#### Why it happens

You opened the file in read mode (`"r"`) but tried to write to it.

#### Fix
```python
with open("deployment.log", "a") as file:
    file.write("Deployment started\n")
```

## 4. CI/CD basics

### Example 1: Simulated build pipeline

```python
# A basic build pipeline simulation.
status = {
    "checkout": True,
    "install_dependencies": True,
    "run_tests": True,
    "build_artifact": True
}

for step, passed in status.items():
    print(f"{step}: {'passed' if passed else 'failed'}")
```

**Why this is useful:**
CI/CD pipelines automate building, testing, and packaging code before deployment.

### Example 2: Build success check

```python
build_success = True
if build_success:
    print("Build succeeded")
else:
    print("Build failed")
```

### Example 3: Release approval logic

```python
tests_passed = True
security_scan_passed = True

if tests_passed and security_scan_passed:
    print("Release approved")
else:
    print("Release blocked")
```

### Common mistakes

#### Correct code
```python
if tests_passed and security_scan_passed:
    print("Release approved")
```

#### Wrong code
```python
if tests_passed or security_scan_passed:
    print("Release approved")
```

#### Why it is wrong

Using `or` allows a release to proceed if only one check passes. In real systems, both checks usually need to pass.

#### Fix
```python
if tests_passed and security_scan_passed:
    print("Release approved")
```

## 5. Docker and container basics

### Example 1: Check if Docker is installed

```python
import shutil

docker_path = shutil.which("docker")
print("Docker installed:" if docker_path else "Docker missing:", bool(docker_path))
```

### Example 2: Simulate container status

```python
containers = ["web", "api", "db"]
for container in containers:
    print(f"Container {container} is running")
```

### Example 3: Basic image name concept

```python
image_name = "my-app:1.0.0"
print(f"Deploying image: {image_name}")
```

**Why this is useful:**
Docker images are central to modern DevOps workflows.

## 6. Kubernetes and cloud basics

### Example 1: Check deployment name

```python
deployment_name = "web-app"
print(f"Deploying {deployment_name}")
```

### Example 2: Health check status

```python
pod_status = "Ready"
if pod_status == "Ready":
    print("Pod is healthy")
else:
    print("Pod not ready")
```

### Example 3: Replica count check

```python
replicas = 3
if replicas >= 2:
    print("Application has enough replicas")
```

## 7. Python for cloud automation

### Example 1: AWS-like configuration

```python
config = {
    "region": "us-east-1",
    "instance_type": "t3.micro",
    "environment": "production"
}

print(config)
```

### Example 2: Simple resource check

```python
resources = ["cpu", "memory", "disk"]
for resource in resources:
    print(f"Checking {resource}")
```

### Example 3: Deployment gate

```python
deployment_ready = True
if deployment_ready:
    print("Proceed with rollout")
else:
    print("Pause rollout and review")
```

## 8. Monitoring and alerts

### Example 1: CPU threshold check

```python
cpu_usage = 82
if cpu_usage > 80:
    print("Send alert: CPU high")
else:
    print("CPU normal")
```

### Example 2: Memory check

```python
memory_usage = 70
if memory_usage > 75:
    print("Memory alert")
else:
    print("Memory OK")
```

### Example 3: Log filtering

```python
logs = ["INFO app started", "ERROR DB timeout", "INFO request processed"]
for log in logs:
    if "ERROR" in log:
        print(f"Alert: {log}")
```

## Practice tasks

1. Write a script that checks if a folder exists before starting deployment.
2. Write a script that reads a config file and prints only lines that contain `enabled`.
3. Write a script that checks if the required environment variables are set before a deployment.
4. Write a script that loops over a list of services and prints whether each is healthy or not.
5. Write a script that creates a deployment log with timestamps.

## Quick debugging tips

- Check whether the file exists before reading it.
- Check whether environment variables are loaded correctly.
- Use `print()` to inspect config values during deployment scripts.
- Verify that the path is correct before using it in production automation.
- Use `with open(...)` to avoid leaving files open.
- In CI/CD logic, make sure gate conditions are strict enough.

This module gives you the Python foundation needed for DevOps automation, deployment work, and infrastructure scripting.
