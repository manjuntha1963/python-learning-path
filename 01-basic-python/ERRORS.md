# How to Learn From Python Errors

When practising each topic, use this order:

1. **Correct code** — run working code first so you understand the expected result.
2. **Wrong code** — change one small part on purpose.
3. **Error message** — read the last line first; it usually tells you the error type.
4. **Why it happens** — identify which Python rule was broken.
5. **How to fix it** — compare the wrong and correct versions, then run the corrected code.
6. **Practise again** — change the input and confirm the program still works.

## Example: variable name

### Correct code

```python
# Create a variable before using it.
employee_age = 28

# Print the value stored in the variable.
print(employee_age)
```

**What happens:** Python prints `28` because the variable exists before `print()` uses it.

### Wrong code

```python
# Try to print a variable that has not been created yet.
print(employee_age)
```

### Error

```text
NameError: name 'employee_age' is not defined
```

### Why it happens

Python reads instructions from top to bottom. There is no `employee_age` variable when `print()` runs.

### How to fix it

```python
# Create the variable first.
employee_age = 28

# Use it after it has been created.
print(employee_age)
```

## Example: input and numbers

### Correct code

```python
# Convert the text entered by the user into a whole number.
age = int(input("Enter your age: "))

# Add one to calculate the age next year.
print(age + 1)
```

### Wrong code

```python
# input() returns text, not a number.
age = input("Enter your age: ")

# Python cannot add a number to text.
print(age + 1)
```

### Error

```text
TypeError: can only concatenate str (not "int") to str
```

### Why it happens

Even if the user types `28`, `input()` returns the string `"28"`. Python cannot add the integer `1` to a string.

### How to fix it

Use `int()` when you need a whole number, or `float()` when decimal values are allowed:

```python
# int() changes numeric text into an integer.
age = int(input("Enter your age: "))
print(age + 1)
```

## Example: condition indentation

### Correct code

```python
# Store the person's age.
age = 20

# The colon starts the condition's code block.
if age >= 18:
    # Indentation shows that this line belongs to the if statement.
    print("Adult")
```

### Wrong code

```python
age = 20
if age >= 18:
print("Adult")
```

### Error

```text
IndentationError: expected an indented block
```

### Why it happens

Python uses indentation to group code. The `print()` line must be indented beneath the `if` statement.

### How to fix it

```python
age = 20
if age >= 18:
    print("Adult")
```

## Error checklist for every topic

Before asking for help, check:

- Did I type the name exactly the same way everywhere?
- Did I close every bracket, parenthesis, and quotation mark?
- Did I add a colon after `if`, `for`, `while`, `def`, and `class`?
- Is the code inside a block indented consistently?
- Am I mixing text and numbers without converting them?
- Did I read the error type and the line number?
- Can I reproduce the error with a smaller example?

The main beginner topics will use this same format: **correct code first, wrong code second, error message, plain-English reason, and fixed code**.
