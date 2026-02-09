"""
ML Concepts — Exercises
========================

Practice problems to test your understanding of machine learning fundamentals.
Try to solve each exercise before looking at the solutions below.

Run this file:
    python3 exercises.py
"""

import random
import math


# =============================================================================
# EXERCISE 1: Train/Test Split Implementation
# Write a function that splits data into training and testing sets.
# The function should take features (X), labels (y), and test_size.
# Return X_train, X_test, y_train, y_test
# =============================================================================

def exercise_1():
    """Implement a train/test split function."""
    print("Implement train_test_split(X, y, test_size)")
    print()

    def train_test_split(X, y, test_size=0.2):
        # YOUR CODE HERE
        # Hint: Calculate split index, then slice the lists
        split_idx = int(len(X) * (1 - test_size))
        X_train = X[:split_idx]
        X_test = X[split_idx:]
        y_train = y[:split_idx]
        y_test = y[split_idx:]
        return X_train, X_test, y_train, y_test

    # Test it
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    print(f"Original data: {len(X)} examples")
    print(f"Training set: {len(X_train)} examples")
    print(f"Testing set: {len(X_test)} examples")
    print(f"Training X: {X_train}")
    print(f"Testing X: {X_test}")


# =============================================================================
# EXERCISE 2: Calculate MSE (Mean Squared Error)
# Implement a function that calculates the mean squared error between
# predictions and actual values.
# MSE = average of (predicted - actual)²
# =============================================================================

def exercise_2():
    """Calculate Mean Squared Error."""
    print("Calculate MSE between predictions and actual values")
    print()

    def calculate_mse(actual, predicted):
        # YOUR CODE HERE
        # Hint: Sum of squared errors, then divide by count
        total_error = sum((pred - act) ** 2 for pred, act in zip(predicted, actual))
        mse = total_error / len(actual)
        return mse

    # Test cases
    actual = [100, 200, 300, 400, 500]
    predicted1 = [98, 202, 297, 405, 498]  # Very close
    predicted2 = [120, 180, 320, 380, 520]  # Farther off

    mse1 = calculate_mse(actual, predicted1)
    mse2 = calculate_mse(actual, predicted2)

    print(f"Actual values: {actual}")
    print(f"Predictions 1: {predicted1}")
    print(f"MSE 1: {mse1:.2f} (lower is better)")
    print()
    print(f"Predictions 2: {predicted2}")
    print(f"MSE 2: {mse2:.2f} (lower is better)")
    print()
    print(f"Model 1 is better - it has {'lower' if mse1 < mse2 else 'higher'} MSE")


# =============================================================================
# EXERCISE 3: Calculate Accuracy for Classification
# Write a function that calculates classification accuracy.
# Accuracy = (correct predictions) / (total predictions)
# =============================================================================

def exercise_3():
    """Calculate classification accuracy."""
    print("Calculate accuracy of predictions")
    print()

    def calculate_accuracy(actual, predicted):
        # YOUR CODE HERE
        # Hint: Count how many predictions match actual labels
        correct = sum(1 for act, pred in zip(actual, predicted) if act == pred)
        accuracy = correct / len(actual)
        return accuracy

    # Test cases
    actual = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
    predicted1 = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]  # Perfect
    predicted2 = [0, 1, 0, 0, 1, 1, 1, 0, 0, 1]  # Some errors

    acc1 = calculate_accuracy(actual, predicted1)
    acc2 = calculate_accuracy(actual, predicted2)

    print(f"Actual labels: {actual}")
    print(f"Predictions 1: {predicted1}")
    print(f"Accuracy 1: {acc1:.1%}")
    print()
    print(f"Predictions 2: {predicted2}")
    print(f"Accuracy 2: {acc2:.1%}")


# =============================================================================
# EXERCISE 4: Euclidean Distance
# Implement the euclidean distance function for k-NN.
# Distance = sqrt((x1-x2)² + (y1-y2)² + ...)
# =============================================================================

def exercise_4():
    """Calculate euclidean distance between two points."""
    print("Implement euclidean distance for k-NN")
    print()

    def euclidean_distance(point1, point2):
        # YOUR CODE HERE
        # Hint: Sum of squared differences, then take square root
        squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
        return math.sqrt(squared_diff)

    # Test cases
    point_a = [0, 0]
    point_b = [3, 4]
    point_c = [1, 1]

    dist_ab = euclidean_distance(point_a, point_b)
    dist_ac = euclidean_distance(point_a, point_c)
    dist_bc = euclidean_distance(point_b, point_c)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Point C: {point_c}")
    print()
    print(f"Distance A to B: {dist_ab:.2f}")
    print(f"Distance A to C: {dist_ac:.2f}")
    print(f"Distance B to C: {dist_bc:.2f}")
    print()
    print(f"Point C is closest to Point {'A' if dist_ac < dist_bc else 'B'}")


# =============================================================================
# EXERCISE 5: Feature Normalization
# Normalize features to 0-1 range.
# normalized = (value - min) / (max - min)
# =============================================================================

def exercise_5():
    """Normalize features to 0-1 range."""
    print("Normalize a list of values to 0-1 range")
    print()

    def normalize(values):
        # YOUR CODE HERE
        # Hint: Find min and max, then apply formula to each value
        min_val = min(values)
        max_val = max(values)
        if max_val == min_val:
            return [0.5] * len(values)
        normalized = [(v - min_val) / (max_val - min_val) for v in values]
        return normalized

    # Test cases
    prices = [50000, 100000, 150000, 200000, 250000]
    ages = [1, 5, 10, 20, 50]

    normalized_prices = normalize(prices)
    normalized_ages = normalize(ages)

    print("House prices (original):", prices)
    print("House prices (normalized):", [f"{x:.2f}" for x in normalized_prices])
    print()
    print("House ages (original):", ages)
    print("House ages (normalized):", [f"{x:.2f}" for x in normalized_ages])
    print()
    print("Now both features are on the same 0-1 scale!")


# =============================================================================
# EXERCISE 6: Simple Linear Predictor
# Implement a simple linear prediction function and calculate predictions.
# Then determine which set of parameters gives better predictions.
# =============================================================================

def exercise_6():
    """Compare different model parameters."""
    print("Compare two models with different parameters")
    print()

    def predict_linear(x, weight, bias):
        # YOUR CODE HERE
        # Hint: Linear model is y = weight * x + bias
        return weight * x + bias

    def calculate_mse(actual, predicted):
        total_error = sum((pred - act) ** 2 for pred, act in zip(predicted, actual))
        return total_error / len(actual)

    # True data: y = 3x + 5
    X = [1, 2, 3, 4, 5]
    y_actual = [8, 11, 14, 17, 20]

    # Two different models
    model1_weight, model1_bias = 3, 5  # Close to truth
    model2_weight, model2_bias = 2, 10  # Further from truth

    # Make predictions
    predictions1 = [predict_linear(x, model1_weight, model1_bias) for x in X]
    predictions2 = [predict_linear(x, model2_weight, model2_bias) for x in X]

    # Calculate errors
    mse1 = calculate_mse(y_actual, predictions1)
    mse2 = calculate_mse(y_actual, predictions2)

    print(f"Actual values: {y_actual}")
    print(f"True relationship: y = 3x + 5")
    print()
    print(f"Model 1 (weight={model1_weight}, bias={model1_bias}):")
    print(f"  Predictions: {predictions1}")
    print(f"  MSE: {mse1:.2f}")
    print()
    print(f"Model 2 (weight={model2_weight}, bias={model2_bias}):")
    print(f"  Predictions: {predictions2}")
    print(f"  MSE: {mse2:.2f}")
    print()
    print(f"Winner: Model {1 if mse1 < mse2 else 2} (lower MSE is better)")


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    """
    Solution: Train/Test Split

    Key concepts:
    - Calculate split index: int(len(data) * (1 - test_size))
    - Use slicing to split both X and y
    - Return four arrays: X_train, X_test, y_train, y_test
    """
    print("SOLUTION 1: Train/Test Split")
    print()
    print("def train_test_split(X, y, test_size=0.2):")
    print("    split_idx = int(len(X) * (1 - test_size))")
    print("    X_train = X[:split_idx]")
    print("    X_test = X[split_idx:]")
    print("    y_train = y[:split_idx]")
    print("    y_test = y[split_idx:]")
    print("    return X_train, X_test, y_train, y_test")
    print()
    print("Important: In practice, shuffle data before splitting!")


def solution_2():
    """
    Solution: Mean Squared Error

    Key concepts:
    - Calculate error for each prediction: (predicted - actual)²
    - Sum all errors
    - Divide by number of samples
    - Lower MSE = better predictions
    """
    print("SOLUTION 2: MSE Calculation")
    print()
    print("def calculate_mse(actual, predicted):")
    print("    total_error = sum((pred - act) ** 2")
    print("                      for pred, act in zip(predicted, actual))")
    print("    return total_error / len(actual)")
    print()
    print("Why square the errors?")
    print("- Penalizes large errors more heavily")
    print("- Eliminates negative values (errors cancel out)")
    print("- Mathematically convenient for optimization")


def solution_3():
    """
    Solution: Classification Accuracy

    Key concepts:
    - Count correct predictions
    - Divide by total predictions
    - Result is between 0 (terrible) and 1 (perfect)
    - Accuracy can be misleading with imbalanced classes
    """
    print("SOLUTION 3: Accuracy Calculation")
    print()
    print("def calculate_accuracy(actual, predicted):")
    print("    correct = sum(1 for act, pred in zip(actual, predicted)")
    print("                  if act == pred)")
    print("    return correct / len(actual)")
    print()
    print("Warning: Accuracy isn't always the best metric!")
    print("Example: If 95% of emails are not spam, a model that")
    print("always predicts 'not spam' gets 95% accuracy but is useless.")


def solution_4():
    """
    Solution: Euclidean Distance

    Key concepts:
    - Calculate squared difference for each dimension
    - Sum all squared differences
    - Take square root
    - Used in k-NN to find nearest neighbors
    """
    print("SOLUTION 4: Euclidean Distance")
    print()
    print("def euclidean_distance(point1, point2):")
    print("    squared_diff = sum((a - b) ** 2")
    print("                       for a, b in zip(point1, point2))")
    print("    return math.sqrt(squared_diff)")
    print()
    print("Example: Distance from (0,0) to (3,4)")
    print("  squared_diff = (0-3)² + (0-4)² = 9 + 16 = 25")
    print("  distance = √25 = 5")
    print()
    print("This is the Pythagorean theorem extended to n dimensions!")


def solution_5():
    """
    Solution: Feature Normalization

    Key concepts:
    - Brings all features to same scale (0-1)
    - Formula: (value - min) / (max - min)
    - Prevents features with larger ranges from dominating
    - Important for algorithms that use distance (k-NN, neural nets)
    """
    print("SOLUTION 5: Normalization")
    print()
    print("def normalize(values):")
    print("    min_val = min(values)")
    print("    max_val = max(values)")
    print("    normalized = [(v - min_val) / (max_val - min_val)")
    print("                  for v in values]")
    print("    return normalized")
    print()
    print("Why normalize?")
    print("- House size: 1000-3000 sq ft (range: 2000)")
    print("- Bedrooms: 1-5 (range: 4)")
    print("Without normalization, size dominates distance calculations!")
    print("After normalization, both features equally important.")


def solution_6():
    """
    Solution: Linear Predictor

    Key concepts:
    - Linear model: y = weight * x + bias
    - Weight: how much x affects output (slope)
    - Bias: base value when x=0 (y-intercept)
    - Training means finding best weight and bias
    """
    print("SOLUTION 6: Linear Prediction")
    print()
    print("def predict_linear(x, weight, bias):")
    print("    return weight * x + bias")
    print()
    print("This is the simplest machine learning model!")
    print()
    print("Components:")
    print("- weight: learned parameter (slope)")
    print("- bias: learned parameter (intercept)")
    print("- x: input feature")
    print("- output: prediction")
    print()
    print("Training = finding weight and bias that minimize MSE")


# =============================================================================
# Main runner
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Train/Test Split", exercise_1),
        ("Mean Squared Error", exercise_2),
        ("Classification Accuracy", exercise_3),
        ("Euclidean Distance", exercise_4),
        ("Feature Normalization", exercise_5),
        ("Linear Predictor Comparison", exercise_6),
    ]

    solutions = [
        ("Train/Test Split", solution_1),
        ("Mean Squared Error", solution_2),
        ("Classification Accuracy", solution_3),
        ("Euclidean Distance", solution_4),
        ("Feature Normalization", solution_5),
        ("Linear Predictor", solution_6),
    ]

    # Run exercises
    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 70)
        print(f"EXERCISE {i}: {title}")
        print("=" * 70)
        func()
        print()

    # Separator before solutions
    print("\n" + "=" * 70)
    print("SOLUTIONS")
    print("=" * 70)
    print()

    # Run solutions
    for i, (title, func) in enumerate(solutions, 1):
        print("-" * 70)
        func()
        print()
