# 01 - Basic Python

This module starts with the smallest Python ideas. The examples use normal English and explain the purpose of the code.

## 1. `print()` and comments

### Example 1: Print a welcome message

A `print()` statement displays text on the screen. We use it to show a message to a user.

```python
# print() is a built-in Python function.
# We use it to display text in the terminal.
print("Welcome to Python")
```

### Example 2: Print two messages

Python runs statements from top to bottom. We use two `print()` statements when we want two separate lines.

```python
# This line displays the first message.
print("I am learning Python")

# This line displays the second message on a new line.
print("I will practise every day")
```

### Example 3: Print a calculation

Python can calculate before it displays a result. We do not put the calculation inside quotes because it is a number expression, not text.

```python
# Store two numbers directly in an addition expression.
# The + operator adds the numbers together.
print(10 + 5)
```

### Common mistakes

#### Correct code

```python
print("Welcome to Python")
```

#### Wrong code

```python
print "Welcome to Python"
```

#### Error

```text
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

#### Why it happens

In Python 3, `print` is a function and must use parentheses. Older Python versions allowed `print` without parentheses, but Python 3 requires them.

#### How to fix it

```python
print("Welcome to Python")
```

**Practise:** Print your name, your learning goal, and the result of `25 - 7`.

---

## 2. Variables and names

A variable is a named container for a value. A descriptive name tells the reader what the value means.

### Example 1: Store an age

```python
# employee_age is the variable name.
# We use a clear name so another person understands the value.
# 28 is an integer, which means a whole number.
employee_age = 28

# print() displays the value stored in employee_age.
print(employee_age)
```

### Example 2: Store a person's name

```python
# employee_name is a variable that stores text.
# Text values must be surrounded by quotation marks.
employee_name = "Asha"

# We use the variable instead of repeating the text in many places.
print(employee_name)
```

### Example 3: Change a variable

Variables can be updated when information changes. This is why variables are more useful than writing a value repeatedly.

```python
# Store the first number of tasks.
tasks_completed = 2

# Add one task to the existing value.
# The new value replaces the old value in the variable.
tasks_completed = tasks_completed + 1

# Display the updated value.
print(tasks_completed)
```

### Common mistakes

#### Correct code

```python
student_name = "Priya"
print(student_name)
```

#### Wrong code

```python
print(student_name)
student_name = "Priya"
```

#### Error

```text
NameError: name 'student_name' is not defined
```

#### Why it happens

Python reads code from top to bottom. The variable `student_name` is created only after `print(student_name)` runs.

#### How to fix it

```python
student_name = "Priya"
print(student_name)
```

**Naming rule:** Use `snake_case`, such as `employee_age`. Avoid unclear names such as `a` unless the meaning is obvious in a very small loop.

**Practise:** Create variables named `student_name`, `course_name`, and `lessons_completed`, then print them.

---

## 3. Basic data types

A data type describes what kind of value a variable contains.

### Example 1: Text (`str`)

```python
# A string is text inside quotation marks.
city_name = "London"

# type() tells us the kind of value stored in city_name.
print(type(city_name))
```

### Example 2: Whole and decimal numbers (`int` and `float`)

```python
# An int stores a whole number without a decimal part.
item_count = 3

# A float stores a number that can have a decimal part.
item_price = 19.99

# Multiplication calculates the total price.
print(item_count * item_price)
```

### Example 3: True or false (`bool`)

```python
# A Boolean stores one of two values: True or False.
is_logged_in = True

# if checks the Boolean value before running the message.
if is_logged_in:
    # This line runs because is_logged_in is True.
    print("Welcome back")
```

### Common mistakes

#### Correct code

```python
city_name = "London"
print(city_name)
```

#### Wrong code

```python
city_name = London
print(city_name)
```

#### Error

```text
NameError: name 'London' is not defined
```

#### Why it happens

Without quotation marks, Python treats `London` as a variable name instead of text.

#### How to fix it

```python
city_name = "London"
print(city_name)
```

**Practise:** Create one string, one integer, one float, and one Boolean. Print each value and its type.

---

## 4. User input and conversion

`input()` reads text typed by a user. Input is always returned as a string, so we convert it when we need a number.

### Example 1: Ask for a name

```python
# input() pauses the program and waits for the user to type text.
user_name = input("What is your name? ")

# f-string inserts the value of user_name into the message.
print(f"Hello, {user_name}!")
```

### Example 2: Add two numbers

```python
# input() returns text, even when the user types a number.
first_text = input("Enter the first number: ")
second_text = input("Enter the second number: ")

# int() converts each text value into a whole number.
first_number = int(first_text)
second_number = int(second_text)

# Add the converted numbers and display the result.
print(first_number + second_number)
```

### Example 3: Calculate age next year

```python
# Ask the user for an age and convert the answer to an integer.
current_age = int(input("How old are you? "))

# Add one because the question asks for next year's age.
next_year_age = current_age + 1

# Display the calculated value in a complete sentence.
print(f"Next year you will be {next_year_age}.")
```

### Common mistakes

#### Correct code

```python
age = int(input("How old are you? "))
print(age + 1)
```

#### Wrong code

```python
age = input("How old are you? ")
print(age + 1)
```

#### Error

```text
TypeError: can only concatenate str (not "int") to str
```

#### Why it happens

`input()` returns text, but `+ 1` needs a number. The text and the number cannot be added directly.

#### How to fix it

```python
age = int(input("How old are you? "))
print(age + 1)
```

**Practise:** Ask for a product price and quantity, convert both to numbers, and print the total.

---

## 5. Operators

Operators perform actions such as addition, comparison, and logical checking.

### Example 1: Shopping total

```python
# Store the price of one notebook.
price = 4.50

# Store how many notebooks the customer wants.
quantity = 3

# The * operator multiplies the price by the quantity.
total = price * quantity

# Display the total amount.
print(total)
```

### Example 2: Compare a score

```python
# Store a student's score.
score = 75

# The >= operator asks whether score is at least 50.
passed = score >= 50

# The result is a Boolean: True or False.
print(passed)
```

### Example 3: Check two requirements

```python
# Store whether a person has a ticket.
has_ticket = True

# Store whether the event is open.
event_is_open = True

# The and operator requires both conditions to be True.
can_enter = has_ticket and event_is_open

# Display the final Boolean result.
print(can_enter)
```

### Common mistakes

#### Correct code

```python
score = 75
print(score >= 50)
```

#### Wrong code

```python
score = 75
print(score = 50)
```

#### Error

```text
SyntaxError: invalid syntax
```

#### Why it happens

`=` is used to assign a value, while `==` is used to compare values.

#### How to fix it

```python
score = 75
print(score == 50)
```

**Practise:** Use `+`, `-`, `/`, `>`, `==`, and `and` in small examples.

---

## 6. Conditions

Conditions allow a program to choose what to do. Use them when the result depends on information.

### Example 1: Adult or minor

```python
# Store the person's age.
age = 20

# Check whether the age is 18 or more.
if age >= 18:
    # Run this block when the condition is True.
    print("The person is an adult")
else:
    # Run this block when the condition is False.
    print("The person is a minor")
```

### Example 2: Grade with multiple choices

```python
# Store the mark earned by a student.
mark = 82

# Check the highest range first.
if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
else:
    grade = "C or below"

# Display the selected grade.
print(grade)
```

### Example 3: Login decision

```python
# Store the username entered by a user.
username = "admin"

# Store the password entered by a user.
password = "python123"

# The program grants access only when both values match.
if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Login failed")
```

### Common mistakes

#### Correct code

```python
age = 20
if age >= 18:
    print("Adult")
```

#### Wrong code

```python
age = 20
if age >= 18:
print("Adult")
```

#### Error

```text
IndentationError: expected an indented block
```

#### Why it happens

The code inside an `if` block must be indented. Python uses indentation to decide what belongs to the condition.

#### How to fix it

```python
age = 20
if age >= 18:
    print("Adult")
```

**Practise:** Write a condition that prints `Free delivery` when an order total is at least 50.

---

## 7. Loops

A loop repeats code. Use a loop when the same action must happen for several values.

### Example 1: Repeat a message

```python
# range(3) produces the numbers 0, 1, and 2.
for number in range(3):
    # This indented line runs once for each number.
    print("Practise Python")
```

### Example 2: Add sales values

```python
# A list stores several sales values in one variable.
sales = [100, 250, 175]

# Start the total at zero before the loop begins.
total_sales = 0

# The loop takes one sale at a time from the list.
for sale in sales:
    # Add the current sale to the running total.
    total_sales = total_sales + sale

# Display the final total after all values are processed.
print(total_sales)
```

### Example 3: Find a name

```python
# Store several names in a list.
names = ["Asha", "Ben", "Carlos"]

# Check each name one at a time.
for name in names:
    # Compare the current name with the name we want.
    if name == "Ben":
        # Stop the loop when the name is found.
        print("Ben was found")
        break
```

### Common mistakes

#### Correct code

```python
for number in range(3):
    print(number)
```

#### Wrong code

```python
for number in range(3)
    print(number)
```

#### Error

```text
SyntaxError: invalid syntax
```

#### Why it happens

The `for` statement needs a colon at the end. The colon tells Python that a block of code will follow.

#### How to fix it

```python
for number in range(3):
    print(number)
```

**Practise:** Loop through a list of five numbers and print only numbers greater than 10.

---

## 8. Lists and dictionaries

Use a list for an ordered group of values. Use a dictionary for named values stored as key-value pairs.

### Example 1: Add to a list

```python
# A list stores ordered items and allows changes.
tasks = ["Read", "Practise"]

# append() adds a new item to the end of the list.
tasks.append("Review")

# Display all tasks in their current order.
print(tasks)
```

### Example 2: Read a dictionary value

```python
# A dictionary connects a key with a value.
employee = {"name": "Maya", "department": "IT"}

# Use the key "name" to retrieve the employee's name.
print(employee["name"])
```

### Example 3: Update a dictionary

```python
# Store a product and its current price.
product = {"name": "Keyboard", "price": 25}

# Change the value connected to the price key.
product["price"] = 30

# Display the updated dictionary.
print(product)
```

### Common mistakes

#### Correct code

```python
employee = {"name": "Maya", "department": "IT"}
print(employee["name"])
```

#### Wrong code

```python
employee = {"name": "Maya", "department": "IT"}
print(employee[name])
```

#### Error

```text
NameError: name 'name' is not defined
```

#### Why it happens

The key `"name"` in the dictionary is text. Without quotes, Python treats it like a variable name.

#### How to fix it

```python
employee = {"name": "Maya", "department": "IT"}
print(employee["name"])
```

**Practise:** Create a dictionary for a student with a name, course, and score. Update the score and print it.

---

## 9. Functions

A function is a named group of instructions. Use functions to avoid repeating logic and to make code easier to test.

### Example 1: A simple function

```python
# Define a function named say_hello.
def say_hello():
    # This message runs whenever the function is called.
    print("Hello")

# Call the function to run its instructions.
say_hello()
```

### Example 2: A function with an input

```python
# Define a function with a name parameter.
def greet(person_name):
    # Use the supplied parameter in the message.
    print(f"Hello, {person_name}")

# Call the function with a real value.
greet("Asha")
```

### Example 3: A function that returns a result

```python
# Define a function that receives a price and quantity.
def calculate_total(price, quantity):
    # Calculate the result and send it back to the caller.
    return price * quantity

# Store the returned result in a variable.
order_total = calculate_total(10, 3)

# Display the returned result.
print(order_total)
```

### Common mistakes

#### Correct code

```python
def say_hello():
    print("Hello")

say_hello()
```

#### Wrong code

```python
def say_hello():
print("Hello")
```

#### Error

```text
IndentationError: expected an indented block
```

#### Why it happens

Any code inside a function must be indented. Without indentation, Python cannot tell which lines are inside the function.

#### How to fix it

```python
def say_hello():
    print("Hello")
```

**Practise:** Write a `convert_minutes_to_seconds(minutes)` function and return the answer.

---

## Beginner mini-projects

1. **Personal introduction:** Ask for a name, city, and hobby, then print a friendly sentence.
2. **Simple calculator:** Ask for two numbers and display their sum, difference, and product.
3. **Shopping receipt:** Ask for three item prices and print the total.

## What comes next

After these basics are comfortable, the next module will use the same ideas for file automation, command-line scripts, and DevOps tasks. AI, machine learning, AI agents, Agentic AI, and LLM projects will come later and will explain their extra libraries step by step.