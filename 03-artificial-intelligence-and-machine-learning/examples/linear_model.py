# Purpose: Train a simple linear regression model and make a prediction.
# This demonstrates the basic ML workflow: prepare data, fit, predict.

from sklearn.linear_model import LinearRegression

# Prepare training data
# X is the input (features): [[1], [2], [3]] are three training examples
# Note: scikit-learn expects a 2D array, so each value is wrapped in a list
X_train = [[1], [2], [3]]

# y is the output (target): the expected values for each X
# Pattern: y = 2 * X (when X=1, y=2; when X=2, y=4; etc.)
y_train = [2, 4, 6]

# Create and train the model
# fit() learns the pattern from the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Make a prediction for a new input value
# Input: [[4]] (2D array with one sample)
# Expected: approximately 8 (because 2 * 4 = 8)
prediction = model.predict([[4]])[0]
print(f"Input: 4, Predicted output: {prediction}")

# Show what the model learned
print(f"Model learned: y ≈ {model.coef_[0]:.1f} * x + {model.intercept_:.1f}")

print("\nThis is the foundation of ML: learn patterns from data, then predict on new data.")
