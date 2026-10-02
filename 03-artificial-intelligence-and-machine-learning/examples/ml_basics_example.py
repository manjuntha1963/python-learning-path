# Module 03 example: data and model basics
# This shows a simple ML pattern: feature data and a target value.
#
# Common mistake:
# People often pass a 1D list to scikit-learn instead of a 2D array.
# That causes a ValueError because the model expects rows and columns.
#
# Error example:
# X = [1, 2, 3]
# model.fit(X, [2, 4, 6])
# ValueError: Expected 2D array, got 1D array instead
#
# Fix:
# Wrap each input in a list, like [[1], [2], [3]].

from sklearn.linear_model import LinearRegression
import numpy as np

# Input data: a 2D array because scikit-learn expects features in rows and columns
# Each list inside the outer list is one sample
X = np.array([[1], [2], [3], [4]])

# Target output: expected value for each input
# Pattern: y = 2 * x
# So if x=1, y=2; x=2, y=4; etc.
y = np.array([2, 4, 6, 8])

# Create a model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Predict for a new input value
prediction = model.predict([[5]])
print(prediction)

# `coef_` is the learned slope
# `intercept_` is the offset value
print(f"Slope: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
