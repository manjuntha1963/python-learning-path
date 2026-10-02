# 02 - Automation and Scripting

Automation means using Python to do repeatable tasks without manual typing every time. A script is just a Python file that runs instructions one after another.

This module focuses on practical automation tasks that teams use in real work.

## 1. Reading a file

### Example 1: Read a text file

```python
# Open a file in read mode.
# "r" means read only.
file = open("notes.txt", "r")

# Read the entire contents of the file.
content = file.read()

# Print the file content.
print(content)

# Close the file so the system can release resources.
file.close()
```

**Why this is useful:**
You can read application logs, configuration files, reports, and notes automatically.

### Example 2: Read line by line

```python
# Open the file in read mode.
with open("tasks.txt", "r") as file:
    # Read one line at a time.
    for line in file:
        # Print the line after removing extra newline characters.
        print(line.strip())
```

**Why this is useful:**
This is a common pattern for reading logs or processing task lists.

### Example 3: Read a file and count words

```python
# Open the file.
with open("summary.txt", "r") as file:
    text = file.read()

# Split the text into words.
words = text.split()

# Count the words.
print("Total words:", len(words))
```

### Common mistakes

#### Correct code
```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

#### Wrong code
```python
file = open("notes.txt", "r")
print(file.read())
# We forgot to close the file.
```

#### Error
```text
No error in this case, but the file may stay open.
```

#### Why it matters

Leaving files open can create resource leaks, especially in larger systems.

#### Fix
```python
with open("notes.txt", "r") as file:
    print(file.read())
```

## 2. Writing a file

### Example 1: Create a new file and write text

```python
# Open a file in write mode.
# "w" creates the file if it does not exist.
with open("report.txt", "w") as file:
    file.write("Daily report\n")
    file.write("Status: Completed\n")
```

**Why this is useful:**
This is used for generating reports, logs, or saved output from scripts.

### Example 2: Append new content to an existing file

```python
# Open the file in append mode.
with open("log.txt", "a") as file:
    file.write("Application started\n")
```

**Why this is useful:**
Use append mode when storing history or logs over time.

### Example 3: Save a list of names to a file

```python
names = ["Asha", "Ravi", "Maya"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
```

### Common mistakes

#### Correct code
```python
with open("data.txt", "w") as file:
    file.write("hello")
```

#### Wrong code
```python
with open("data.txt", "r") as file:
    file.write("hello")
```

#### Error
```text
io.UnsupportedOperation: not writable
```

#### Why it happens

The file was opened in read mode (`"r"`), so Python cannot write to it.

#### Fix
```python
with open("data.txt", "w") as file:
    file.write("hello")
```

## 3. Automating repeated tasks with loops

### Example 1: Rename files with a number

```python
from pathlib import Path

# Get all text files in a folder.
for index, file in enumerate(Path("documents").glob("*.txt"), start=1):
    new_name = file.with_name(f"document_{index}.txt")
    file.rename(new_name)
    print(f"Renamed to {new_name.name}")
```

**Why this is useful:**
This is used in file cleanup, report naming, and bulk processing.

### Example 2: Create many files automatically

```python
for number in range(1, 6):
    file_name = f"file_{number}.txt"
    with open(file_name, "w") as file:
        file.write(f"This is file {number}\n")
```

**Why this is useful:**
Useful for generating test files, templates, or sample output.

### Example 3: Check folder content

```python
from pathlib import Path

for file in Path(".").iterdir():
    if file.is_file():
        print(file.name)
```

## 4. Reading command-line arguments

### Example 1: Pass a name from the terminal

```python
import sys

name = sys.argv[1]
print(f"Hello, {name}!")
```

Run it like this:
```bash
python script.py Asha
```

**Why this is useful:**
You can build scripts that accept user input at runtime without editing code.

### Example 2: Pass two numbers and calculate sum

```python
import sys

first = int(sys.argv[1])
second = int(sys.argv[2])
print(first + second)
```

Run it like this:
```bash
python script.py 10 20
```

### Example 3: Use argparse for cleaner scripts

```python
import argparse

parser = argparse.ArgumentParser(description="Add two numbers")
parser.add_argument("first", type=int)
parser.add_argument("second", type=int)
args = parser.parse_args()

print(args.first + args.second)
```

**Why this is useful:**
`argparse` helps you create professional scripts with clear parameter handling.

## 5. Automation in real jobs

### Example 1: Email notification script

```python
# This is a basic structure for an automation script.
# In real work, you would use smtplib and a mail server.
message = "Deployment completed successfully."
print(message)
```

### Example 2: Daily report generator

```python
# Generate a file from data.
report_lines = ["Sales: 1200", "Profit: 300", "Status: good"]

with open("daily_report.txt", "w") as file:
    for line in report_lines:
        file.write(line + "\n")
```

### Example 3: System cleanup script

```python
from pathlib import Path

for file in Path("logs").glob("*.log"):
    if file.stat().st_size > 10000:
        print(f"Large log found: {file.name}")
```

## 6. DevOps automation use case

Python is often used in DevOps to automate infrastructure and deployment tasks.

### Example: check a deployment folder

```python
from pathlib import Path

release_folder = Path("releases")

if release_folder.exists():
    for item in release_folder.iterdir():
        print(item.name)
else:
    print("Release folder not found")
```

**Real-world use:**
A release script can check that a build folder exists before deployment.

## 7. AI/LLM automation use case

Python helps process data before AI models are trained or used.

### Example: prepare text files for an AI workflow

```python
with open("input.txt", "r") as file:
    text = file.read()

# Simple preprocessing
cleaned = text.lower().replace("\n", " ")

with open("cleaned_text.txt", "w") as file:
    file.write(cleaned)
```

**Real-world use:**
This is a basic preprocessing step before sending text to an LLM or ML model.

## Practice tasks

1. Write a script that reads a file and prints the number of lines.
2. Write a script that creates five files named `task_1.txt` to `task_5.txt`.
3. Write a script that reads a file and counts how many times the word `error` appears.
4. Write a script that accepts a file name from the command line and prints its first 10 lines.
5. Write a script that reads all files in a folder and lists only `.txt` files.

## Quick debugging tips

- Make sure the file path is correct.
- Check whether you opened the file in the right mode: `r`, `w`, `a`.
- If the script fails with `FileNotFoundError`, check the folder and file name.
- Use `with open(...)` to avoid leaving files open.
- Use `print()` during debugging to see intermediate values.

This topic is a bridge between beginner Python and practical real-world automation work.