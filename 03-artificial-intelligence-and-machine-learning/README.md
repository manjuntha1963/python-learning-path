# 03 - Artificial Intelligence and Machine Learning

Artificial Intelligence (AI) means building systems that can do tasks that normally need human thinking. Machine Learning (ML) is a part of AI where the system learns patterns from data instead of being explicitly programmed for every rule.

This module explains the basics in plain English and uses simple Python examples.

## 1. What is AI and ML?

### Example 1: Spam detection

```python
# Example data for emails.
emails = [
    "win free money now",
    "team meeting at 3 pm",
    "claim your prize",
    "project update attached"
]

# A very simple rule-based filter.
for email in emails:
    if "free" in email.lower() or "win" in email.lower():
        print(f"Possible spam: {email}")
    else:
        print(f"Likely normal email: {email}")
```

**Why this is useful:**
A basic AI/ML system starts with patterns. Here, the script checks for words that often appear in spam emails.

### Example 2: House price estimate

```python
# Example training data
sizes = [1200, 1500, 2000, 2500]
prices = [180000, 220000, 300000, 370000]

# A simple calculation for a rough estimate
sample_size = 2000
estimated_price = 150 + sample_size
print(f"Estimated house price: ${estimated_price}")
```

**Why this is useful:**
Real ML models learn from data; this is a very simple model idea.

### Example 3: Customer behavior prediction

```python
# A simple rule for repeat customers
customer_data = [
    {"spent": 500, "repeat": True},
    {"spent": 100, "repeat": False},
    {"spent": 700, "repeat": True}
]

for customer in customer_data:
    if customer["spent"] > 400:
        print("Likely repeat customer")
    else:
        print("Less likely repeat customer")
```

### Common mistakes

#### Correct code
```python
values = [1, 2, 3]
print(values[0])
```

#### Wrong code
```python
values = [1, 2, 3]
print(values[3])
```

#### Error
```text
IndexError: list index out of range
```

#### Why it happens

A list with 3 items has indexes 0, 1, and 2. Index 3 does not exist.

#### Fix
```python
values = [1, 2, 3]
print(values[2])
```

## 2. Data basics for AI/ML

Machine learning depends on data. We usually store data in tables, lists, or dictionaries.

### Example 1: Store student scores

```python
student_scores = {
    "Asha": 95,
    "Ravi": 80,
    "Maya": 88
}

for student, score in student_scores.items():
    print(f"{student}: {score}")
```

**Why this is useful:**
ML models often work with structured data like names and scores.

### Example 2: Store hotel booking data

```python
bookings = [
    {"city": "Paris", "days": 3, "booked": True},
    {"city": "London", "days": 2, "booked": False},
    {"city": "Rome", "days": 5, "booked": True}
]

for booking in bookings:
    if booking["booked"]:
        print(f"Booked trip to {booking['city']}")
```

### Example 3: Store numbers in a list

```python
# A list is a simple data structure.
prices = [1200, 1400, 1700, 1800]

average = sum(prices) / len(prices)
print(f"Average price: {average}")
```

### Common mistakes

#### Correct code
```python
data = {"sales": 1000}
print(data["sales"])
```

#### Wrong code
```python
data = {"sales": 1000}
print(data["Sales"])
```

#### Error
```text
KeyError: 'Sales'
```

#### Why it happens

Dictionary keys are case-sensitive. `"sales"` and `"Sales"` are different strings.

#### Fix
```python
data = {"sales": 1000}
print(data["sales"])
```

## 3. NumPy for numeric data

NumPy is a Python library used for fast numerical work.

### Example 1: Make a list into a NumPy array

```python
import numpy as np

numbers = [10, 20, 30, 40]
array = np.array(numbers)
print(array)
```

**Why this is useful:**
ML models use arrays and matrices for large data calculations.

### Example 2: Calculate mean value

```python
import numpy as np

values = np.array([10, 20, 30, 40])
print(np.mean(values))
```

### Example 3: Create a 2D array

```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print(matrix.shape)
```

### Common mistakes

#### Correct code
```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr.mean())
```

#### Wrong code
```python
import numpy as np
arr = [1, 2, 3]
print(arr.mean())
```

#### Error
```text
AttributeError: 'list' object has no attribute 'mean'
```

#### Why it happens

`mean()` is a NumPy array method, not a built-in list method.

#### Fix
```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr.mean())
```

## 4. Pandas for tabular data

Pandas is used to work with tables called DataFrames.

### Example 1: Create a small table

```python
import pandas as pd

students = {
    "name": ["Asha", "Ravi", "Maya"],
    "score": [90, 80, 88]
}

df = pd.DataFrame(students)
print(df)
```

### Example 2: Show the average score

```python
import pandas as pd

students = {
    "name": ["Asha", "Ravi", "Maya"],
    "score": [90, 80, 88]
}

df = pd.DataFrame(students)
print(df["score"].mean())
```

### Example 3: Filter data

```python
import pandas as pd

students = {
    "name": ["Asha", "Ravi", "Maya"],
    "score": [90, 80, 88]
}

df = pd.DataFrame(students)
filtered = df[df["score"] >= 85]
print(filtered)
```

### Common mistakes

#### Correct code
```python
import pandas as pd

df = pd.DataFrame({"score": [90, 80]})
print(df["score"].mean())
```

#### Wrong code
```python
import pandas as pd

df = pd.DataFrame({"score": [90, 80]})
print(df.mean())
```

#### Error
```text
TypeError: could not convert string to float
```

#### Why it happens

This example may fail because the DataFrame contains columns that are not numeric; `.mean()` on a DataFrame may work only on numeric columns. The real issue is that you must select the exact column you want.

#### Fix
```python
import pandas as pd

df = pd.DataFrame({"score": [90, 80]})
print(df["score"].mean())
```

## 5. Machine learning basics with scikit-learn

Scikit-learn is a library that gives you tools to train models.

### Example 1: Simple linear regression

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[5]]))
```

**Why this is useful:**
This learns a pattern from data and can predict a new value.

### Example 2: Simple classification example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"Model accuracy: {score}")
```

### Example 3: Make a prediction

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([1, 3, 5, 7])

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[10]])
print(predicted)
```

### Common mistakes

#### Correct code
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression()
model.fit(X, y)
print(model.predict([[5]]))
```

#### Wrong code
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = [1, 2, 3]
y = [2, 4, 6]
model = LinearRegression()
model.fit(X, y)
```

#### Error
```text
ValueError: Expected 2D array, got 1D array instead
```

#### Why it happens

Scikit-learn expects features in a 2D array. A simple list of numbers is 1D and is not enough for most models.

#### Fix
```python
X = np.array([[1], [2], [3]])
```

## 6. Model evaluation

A model is not useful unless we test how well it works.

### Example 1: Accuracy score

```python
from sklearn.metrics import accuracy_score

actual = [1, 0, 1, 1]
predicted = [1, 0, 0, 1]
print(accuracy_score(actual, predicted))
```

### Example 2: Mean squared error

```python
from sklearn.metrics import mean_squared_error

actual = [10, 20, 30]
predicted = [12, 18, 31]
print(mean_squared_error(actual, predicted))
```

### Example 3: Model quality concept

```python
# Model quality is not only about output.
# Accuracy, precision, recall, and error rate are all used in real projects.
print("Model evaluation helps us check if the model is reliable.")
```

**Why this is useful:**
You need to evaluate the model before using it in a real product.

## 7. AI use cases

### Example 1: Image classification

```python
# In real AI projects, images are processed by a model such as a CNN.
print("An image recognition model can identify cats, dogs, or objects.")
```

### Example 2: Predicting sales

```python
# A model can learn from last year's sales, promotions, and weather to predict new sales.
print("This is a common machine learning use case in business.")
```

### Example 3: Chatbot and LLM workflow

```python
# A chatbot uses an LLM model to answer questions in natural language.
print("Large language models read text and generate human-like responses.")
```

## 8. AI ethics and practical thinking

AI is useful, but it must be used responsibly.

### Example 1: Bias in data

```python
# If training data is unfair, the model may produce unfair results.
print("Always check whether your data is balanced and fair.")
```

### Example 2: Data quality

```python
# Bad data gives bad results.
print("Clean data is more important than fancy models.")
```

### Example 3: Human review

```python
# AI provides suggestions, but people still need to check final decisions.
print("Use AI to assist people, not to replace human judgment completely.")
```

## Practice tasks

1. Create a list of 10 numbers and find the mean using NumPy.
2. Create a DataFrame with student names and marks, then print the average.
3. Use scikit-learn to train a simple model and print the prediction.
4. Build a simple spam detector using keywords.
5. Compare two different AI use cases: image recognition and customer churn prediction.

## Quick debugging tips

- Check shapes of arrays and DataFrames.
- Use `print()` to inspect the data before training.
- Make sure your data is numeric when using ML libraries.
- If you get `ValueError`, check whether your array is 1D or 2D.
- Read the error message carefully; many ML errors are about data shape or type.

This topic introduces the core ideas behind AI and ML while keeping the examples easy to understand.