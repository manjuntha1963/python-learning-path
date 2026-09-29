# Python Errors: Three Examples for Every Beginner Topic

Yes. This single file contains **three error examples for every beginner topic**.

Use this order every time:

1. Run the correct code.
2. Run the wrong code intentionally.
3. Read the error type and line number.
4. Understand why it happened.
5. Apply the fix and run the code again.

> Some mistakes produce a Python error. Other mistakes produce a result that is technically valid but logically wrong. Both are important to practise.

## 1. `print()` and comments

### Error 1: Missing parentheses

**Correct code:**
```python
print("Hello")
```

**Wrong code:**
```python
print "Hello"
```

**Error:** `SyntaxError: Missing parentheses in call to 'print'`

**Why:** In Python 3, `print` is a function and needs parentheses.

**Fix:**
```python
print("Hello")
```

### Error 2: Missing quotation marks

**Correct code:**
```python
print("Welcome to Python")
```

**Wrong code:**
```python
print(Welcome to Python)
```

**Error:** `SyntaxError` or `NameError`

**Why:** Text must be inside matching quotation marks. Without them, Python treats the words as code.

**Fix:**
```python
print("Welcome to Python")
```

### Error 3: Unclosed quotation mark

**Correct code:**
```python
print("Python is fun")
```

**Wrong code:**
```python
print("Python is fun)
```

**Error:** `SyntaxError: unterminated string literal`

**Why:** The opening double quote has no closing double quote.

**Fix:**
```python
print("Python is fun")
```

## 2. Variables and names

### Error 1: Using a variable too early

**Correct code:**
```python
employee_age = 28
print(employee_age)
```

**Wrong code:**
```python
print(employee_age)
employee_age = 28
```

**Error:** `NameError: name 'employee_age' is not defined`

**Why:** Python reads from top to bottom. The variable does not exist when it is printed.

**Fix:** Create the variable before using it.

### Error 2: Invalid space in a name

**Correct code:**
```python
employee_age = 28
```

**Wrong code:**
```python
employee age = 28
```

**Error:** `SyntaxError: invalid syntax`

**Why:** Spaces are not allowed inside variable names.

**Fix:** Use snake_case with an underscore: `employee_age`.

### Error 3: Name spelling does not match

**Correct code:**
```python
course_name = "Python"
print(course_name)
```

**Wrong code:**
```python
course_name = "Python"
print(course)
```

**Error:** `NameError: name 'course' is not defined`

**Why:** `course` and `course_name` are two different names.

**Fix:** Use exactly the same name everywhere.

## 3. Basic data types

### Error 1: Text without quotes

**Correct code:**
```python
city_name = "London"
```

**Wrong code:**
```python
city_name = London
```

**Error:** `NameError: name 'London' is not defined`

**Why:** Python thinks `London` is a variable instead of text.

**Fix:** Put text inside quotes.

### Error 2: Adding text and a number

**Correct code:**
```python
item_count = 3
print(item_count + 2)
```

**Wrong code:**
```python
item_count = "3"
print(item_count + 2)
```

**Error:** `TypeError: can only concatenate str (not "int") to str`

**Why:** `"3"` is a string, while `2` is an integer. Python cannot add these types directly.

**Fix:** Remove the quotes or convert the text with `int()`.

### Error 3: Lowercase Boolean

**Correct code:**
```python
is_ready = True
```

**Wrong code:**
```python
is_ready = true
```

**Error:** `NameError: name 'true' is not defined`

**Why:** Python Boolean values are exactly `True` and `False`, with capital letters.

**Fix:**
```python
is_ready = True
```

## 4. User input and conversion

### Error 1: Using input as a number

**Correct code:**
```python
age = int(input("Age: "))
print(age + 1)
```

**Wrong code:**
```python
age = input("Age: ")
print(age + 1)
```

**Error:** `TypeError: can only concatenate str (not "int") to str`

**Why:** `input()` always returns text.

**Fix:** Convert it with `int()` for whole numbers or `float()` for decimals.

### Error 2: Invalid numeric input

**Correct code:**
```python
number = int("25")
print(number)
```

**Wrong code:**
```python
number = int("twenty-five")
```

**Error:** `ValueError: invalid literal for int()`

**Why:** `int()` can convert numeric text, but not words.

**Fix:** Ask the user for digits or handle the error with `try` and `except`.

### Error 3: Wrong variable name in an f-string

**Correct code:**
```python
user_name = "Asha"
print(f"Hello, {user_name}")
```

**Wrong code:**
```python
user_name = "Asha"
print(f"Hello, {username}")
```

**Error:** `NameError: name 'username' is not defined`

**Why:** The created name is `user_name`, not `username`.

**Fix:** Match the variable name exactly.

## 5. Operators

### Error 1: Confusing `=` and `==`

**Correct code:**
```python
score = 75
print(score == 75)
```

**Wrong code:**
```python
score = 75
print(score = 75)
```

**Error:** `SyntaxError: invalid syntax`

**Why:** `=` assigns a value; `==` compares two values.

**Fix:** Use `==` when asking a comparison question.

### Error 2: Dividing by zero

**Correct code:**
```python
items = 10
people = 2
print(items / people)
```

**Wrong code:**
```python
print(10 / 0)
```

**Error:** `ZeroDivisionError: division by zero`

**Why:** Division by zero is mathematically undefined.

**Fix:** Check that the divisor is not zero before dividing.

### Error 3: Comparing different types

**Correct code:**
```python
score = 75
print(score == 75)
```

**Wrong code:**
```python
score = 75
print(score == "75")
```

**Result:** `False`

**Why:** The number `75` and the text `"75"` are different types. This is a logic mistake, not a syntax error.

**Fix:** Convert or use the same type on both sides.

## 6. Conditions

### Error 1: Missing colon

**Correct code:**
```python
if age >= 18:
    print("Adult")
```

**Wrong code:**
```python
if age >= 18
    print("Adult")
```

**Error:** `SyntaxError: invalid syntax`

**Why:** Python requires a colon before the indented block.

**Fix:** Add `:` after the condition.

### Error 2: Missing indentation

**Correct code:**
```python
if age >= 18:
    print("Adult")
```

**Wrong code:**
```python
if age >= 18:
print("Adult")
```

**Error:** `IndentationError: expected an indented block`

**Why:** Python uses indentation to show which code belongs to the `if` statement.

**Fix:** Indent the block, normally with four spaces.

### Error 3: Wrong order of `elif` and `else`

**Correct code:**
```python
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C or below")
```

**Wrong code:**
```python
if score >= 90:
    print("A")
else:
    print("C or below")
elif score >= 75:
    print("B")
```

**Error:** `SyntaxError: invalid syntax`

**Why:** `elif` must come before the final `else`.

**Fix:** Put all `elif` branches before `else`.

## 7. Loops

### Error 1: Missing colon after `for`

**Correct code:**
```python
for number in range(3):
    print(number)
```

**Wrong code:**
```python
for number in range(3)
    print(number)
```

**Error:** `SyntaxError: invalid syntax`

**Why:** A loop statement must end with a colon.

**Fix:** Add `:` after `range(3)`.

### Error 2: Missing indentation in a loop

**Correct code:**
```python
for number in range(3):
    print(number)
```

**Wrong code:**
```python
for number in range(3):
print(number)
```

**Error:** `IndentationError: expected an indented block`

**Why:** The repeated code must be inside the loop block.

**Fix:** Indent `print(number)`.

### Error 3: Index outside a list

**Correct code:**
```python
names = ["Asha", "Ben"]
print(names[1])
```

**Wrong code:**
```python
names = ["Asha", "Ben"]
print(names[2])
```

**Error:** `IndexError: list index out of range`

**Why:** A two-item list has indexes `0` and `1`; index `2` does not exist.

**Fix:** Use a valid index or loop through the list.

## 8. Lists and dictionaries

### Error 1: Missing dictionary key

**Correct code:**
```python
employee = {"name": "Maya"}
print(employee["name"])
```

**Wrong code:**
```python
employee = {"name": "Maya"}
print(employee["age"])
```

**Error:** `KeyError: 'age'`

**Why:** The dictionary does not contain an `age` key.

**Fix:** Use an existing key or use `employee.get("age", "Not provided")`.

### Error 2: Using a string index for a list

**Correct code:**
```python
tasks = ["Read", "Practise"]
print(tasks[0])
```

**Wrong code:**
```python
tasks = ["Read", "Practise"]
print(tasks["first"])
```

**Error:** `TypeError: list indices must be integers or slices, not str`

**Why:** Lists use numeric indexes; dictionaries use named keys.

**Fix:** Use `tasks[0]` or change the data to a dictionary.

### Error 3: Calling a list method on a dictionary

**Correct code:**
```python
tasks = ["Read"]
tasks.append("Practise")
```

**Wrong code:**
```python
employee = {"name": "Maya"}
employee.append("IT")
```

**Error:** `AttributeError: 'dict' object has no attribute 'append'`

**Why:** `append()` belongs to lists, not dictionaries.

**Fix:** Add a dictionary key instead: `employee["department"] = "IT"`.

## 9. Functions

### Error 1: Missing colon after `def`

**Correct code:**
```python
def say_hello():
    print("Hello")
```

**Wrong code:**
```python
def say_hello()
    print("Hello")
```

**Error:** `SyntaxError: invalid syntax`

**Why:** A function definition must end with a colon.

**Fix:** Add `:` after the closing parenthesis.

### Error 2: Wrong number of arguments

**Correct code:**
```python
def greet(person_name):
    print(f"Hello, {person_name}")

greet("Asha")
```

**Wrong code:**
```python
def greet(person_name):
    print(f"Hello, {person_name}")

greet("Asha", "Kumar")
```

**Error:** `TypeError: greet() takes 1 positional argument but 2 were given`

**Why:** The function defines one parameter but receives two values.

**Fix:** Pass one value or update the function definition to accept two parameters.

### Error 3: Calling a function before defining it

**Correct code:**
```python
def say_hello():
    print("Hello")

say_hello()
```

**Wrong code:**
```python
say_hello()

def say_hello():
    print("Hello")
```

**Error:** `NameError: name 'say_hello' is not defined`

**Why:** Python reaches the call before it has created the function.

**Fix:** Define the function before calling it.

## Debugging checklist

- Read the final line of the error first.
- Look at the line number Python reports.
- Check spelling and capitalization.
- Check quotation marks, brackets, parentheses, and colons.
- Check indentation.
- Check whether values have the correct data type.
- Test the smallest possible version of the code.
- Fix one error at a time.
