"""
ML Concepts — Example Code
============================

This demonstrates fundamental machine learning concepts using pure Python.
No external libraries needed - we'll implement everything from scratch!

Run this file:
    python3 example.py
"""

import random
import math


# ============================================================================
# SECTION 1: What is a "Model"?
# ============================================================================
print("=" * 70)
print("SECTION 1: What is a Model?")
print("=" * 70)
print()

# A model is just a function with learnable parameters
# Let's start with the simplest model: a linear function

def simple_model(x, weight, bias):
    """
    A simple linear model: y = weight * x + bias

    Parameters (learnable):
    - weight: how much x affects the output
    - bias: the base value when x is 0
    """
    return weight * x + bias


# Let's try different parameters
x_value = 5

print("Trying different parameters for the same input:")
print(f"Input x = {x_value}")
print()

# Bad parameters
prediction1 = simple_model(x_value, weight=0, bias=0)
print(f"With weight=0, bias=0: prediction = {prediction1}")

# Better parameters
prediction2 = simple_model(x_value, weight=2, bias=3)
print(f"With weight=2, bias=3: prediction = {prediction2}")

# Different parameters
prediction3 = simple_model(x_value, weight=-1, bias=10)
print(f"With weight=-1, bias=10: prediction = {prediction3}")

print()
print("Key insight: The same model architecture with different parameters")
print("gives different predictions. Training means finding good parameters!")
print()


# ============================================================================
# SECTION 2: Linear Regression from Scratch
# ============================================================================
print("=" * 70)
print("SECTION 2: Linear Regression from Scratch")
print("=" * 70)
print()

# Generate some fake data: house size -> price
# True relationship: price = 100 * size + 50000 (with some noise)
random.seed(42)

sizes = [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
prices = [100 * size + 50000 + random.uniform(-10000, 10000) for size in sizes]

print("Our dataset (House sizes -> Prices):")
for size, price in zip(sizes[:5], prices[:5]):
    print(f"  {size} sq ft -> ${price:,.0f}")
print("  ...")
print()


def predict(x, weight, bias):
    """Make a prediction using current parameters."""
    return weight * x + bias


def calculate_mse(x_data, y_data, weight, bias):
    """
    Calculate Mean Squared Error - how wrong our predictions are.
    Lower is better!
    """
    total_error = 0
    for x, y_actual in zip(x_data, y_data):
        y_predicted = predict(x, weight, bias)
        error = (y_predicted - y_actual) ** 2
        total_error += error

    mse = total_error / len(x_data)
    return mse


def train_linear_regression(x_data, y_data, learning_rate=0.0001, epochs=100):
    """
    Train a linear regression model using gradient descent.

    Gradient descent: iteratively adjust parameters to reduce error.
    Think of it like walking downhill to find the lowest point.
    """
    # Start with random parameters
    weight = random.uniform(0, 1)
    bias = random.uniform(0, 1000)

    print(f"Starting training with weight={weight:.2f}, bias={bias:.2f}")
    print(f"Initial MSE: {calculate_mse(x_data, y_data, weight, bias):,.0f}")
    print()

    n = len(x_data)

    for epoch in range(epochs):
        # Calculate gradients (how to adjust parameters)
        weight_gradient = 0
        bias_gradient = 0

        for x, y_actual in zip(x_data, y_data):
            y_predicted = predict(x, weight, bias)
            error = y_predicted - y_actual

            # Calculus magic: these are the derivatives
            weight_gradient += (2 / n) * error * x
            bias_gradient += (2 / n) * error

        # Update parameters (move downhill)
        weight -= learning_rate * weight_gradient
        bias -= learning_rate * bias_gradient

        # Print progress every 20 epochs
        if (epoch + 1) % 20 == 0:
            mse = calculate_mse(x_data, y_data, weight, bias)
            print(f"Epoch {epoch + 1}: MSE = {mse:,.0f}, weight={weight:.2f}, bias={bias:.0f}")

    print()
    print(f"Final parameters: weight={weight:.2f}, bias={bias:.0f}")
    print("Compare to true relationship: price = 100 * size + 50000")
    print()

    return weight, bias


# Train the model!
trained_weight, trained_bias = train_linear_regression(sizes, prices, learning_rate=0.00000001, epochs=100)


# ============================================================================
# SECTION 3: Making Predictions
# ============================================================================
print("=" * 70)
print("SECTION 3: Making Predictions with Our Trained Model")
print("=" * 70)
print()

# Now use the trained model to predict prices for new houses
new_sizes = [1100, 1500, 2100, 2800]

print("Predictions for new houses:")
for size in new_sizes:
    predicted_price = predict(size, trained_weight, trained_bias)
    print(f"  {size} sq ft -> ${predicted_price:,.0f}")
print()


# ============================================================================
# SECTION 4: Train/Test Split
# ============================================================================
print("=" * 70)
print("SECTION 4: Train/Test Split")
print("=" * 70)
print()

def train_test_split(x_data, y_data, test_size=0.2, random_seed=42):
    """
    Split data into training and testing sets.

    test_size: fraction of data to use for testing (e.g., 0.2 = 20%)
    """
    random.seed(random_seed)

    # Create list of indices
    indices = list(range(len(x_data)))
    random.shuffle(indices)

    # Calculate split point
    split_idx = int(len(x_data) * (1 - test_size))

    # Split indices
    train_indices = indices[:split_idx]
    test_indices = indices[split_idx:]

    # Split data
    x_train = [x_data[i] for i in train_indices]
    y_train = [y_data[i] for i in train_indices]
    x_test = [x_data[i] for i in test_indices]
    y_test = [y_data[i] for i in test_indices]

    return x_train, x_test, y_train, y_test


# Split our house data
x_train, x_test, y_train, y_test = train_test_split(sizes, prices, test_size=0.3)

print(f"Total data: {len(sizes)} houses")
print(f"Training set: {len(x_train)} houses")
print(f"Testing set: {len(x_test)} houses")
print()

print("Training set (what the model learns from):")
for x, y in zip(x_train[:3], y_train[:3]):
    print(f"  {x} sq ft -> ${y:,.0f}")
print()

print("Testing set (what we evaluate on - model hasn't seen these!):")
for x, y in zip(x_test, y_test):
    print(f"  {x} sq ft -> ${y:,.0f}")
print()


# ============================================================================
# SECTION 5: Evaluating with Train and Test MSE
# ============================================================================
print("=" * 70)
print("SECTION 5: Evaluation Metrics - MSE")
print("=" * 70)
print()

# Train only on training data
print("Training model on training data only...")
w, b = train_linear_regression(x_train, y_train, learning_rate=0.00000001, epochs=100)

# Evaluate on both training and test data
train_mse = calculate_mse(x_train, y_train, w, b)
test_mse = calculate_mse(x_test, y_test, w, b)

print(f"Training MSE: {train_mse:,.0f}")
print(f"Testing MSE: {test_mse:,.0f}")
print()

if test_mse < train_mse * 1.5:
    print("Good! Test MSE is close to training MSE - model generalizes well.")
else:
    print("Warning: Test MSE is much higher - possible overfitting!")
print()


# ============================================================================
# SECTION 6: Classification with k-Nearest Neighbors
# ============================================================================
print("=" * 70)
print("SECTION 6: k-Nearest Neighbors Classification")
print("=" * 70)
print()

# Let's classify fruits based on weight and color (0=green, 1=yellow, 2=red)
# 0 = Apple, 1 = Banana

# Features: [weight_grams, color]
# Labels: fruit type (0=Apple, 1=Banana)
fruit_features = [
    [180, 2],  # Apple: 180g, red
    [190, 2],  # Apple: 190g, red
    [170, 2],  # Apple: 170g, red
    [160, 0],  # Apple: 160g, green
    [120, 1],  # Banana: 120g, yellow
    [130, 1],  # Banana: 130g, yellow
    [125, 1],  # Banana: 125g, yellow
    [115, 1],  # Banana: 115g, yellow
]

fruit_labels = [0, 0, 0, 0, 1, 1, 1, 1]  # 0=Apple, 1=Banana

fruit_names = ["Apple", "Banana"]

print("Training data:")
for features, label in zip(fruit_features, fruit_labels):
    print(f"  Weight={features[0]}g, Color={features[1]} -> {fruit_names[label]}")
print()


def euclidean_distance(point1, point2):
    """
    Calculate distance between two points.
    sqrt((x1-x2)^2 + (y1-y2)^2 + ...)
    """
    squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return math.sqrt(squared_diff)


def knn_predict(train_features, train_labels, test_point, k=3):
    """
    k-Nearest Neighbors classification.

    1. Find k nearest training points to test_point
    2. Take majority vote of their labels
    """
    # Calculate distances to all training points
    distances = []
    for train_point, label in zip(train_features, train_labels):
        dist = euclidean_distance(test_point, train_point)
        distances.append((dist, label))

    # Sort by distance and take k nearest
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]

    # Count votes
    votes = {}
    for _, label in k_nearest:
        votes[label] = votes.get(label, 0) + 1

    # Return label with most votes
    predicted_label = max(votes, key=votes.get)
    return predicted_label


# Test k-NN
test_fruits = [
    [175, 2],  # Should be Apple (red, heavy)
    [120, 1],  # Should be Banana (yellow, light)
    [140, 0],  # Ambiguous - green and medium weight
]

print("Predictions using k-NN (k=3):")
for test_point in test_fruits:
    prediction = knn_predict(fruit_features, fruit_labels, test_point, k=3)
    print(f"  Weight={test_point[0]}g, Color={test_point[1]} -> Predicted: {fruit_names[prediction]}")
print()


# ============================================================================
# SECTION 7: Calculating Accuracy
# ============================================================================
print("=" * 70)
print("SECTION 7: Classification Accuracy")
print("=" * 70)
print()

def calculate_accuracy(true_labels, predicted_labels):
    """
    Accuracy = (number of correct predictions) / (total predictions)
    """
    correct = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred)
    total = len(true_labels)
    return correct / total


# Test accuracy on training data (just for demonstration)
train_predictions = []
for features in fruit_features:
    # Predict using all other points (leave-one-out style)
    pred = knn_predict(fruit_features, fruit_labels, features, k=3)
    train_predictions.append(pred)

accuracy = calculate_accuracy(fruit_labels, train_predictions)
print(f"k-NN accuracy on training data: {accuracy:.1%}")
print("(Note: This isn't a proper evaluation - we should use a test set!)")
print()


# ============================================================================
# SECTION 8: Overfitting Demonstration
# ============================================================================
print("=" * 70)
print("SECTION 8: Overfitting Demonstration")
print("=" * 70)
print()

# Create data with noise
random.seed(42)
clean_x = list(range(1, 11))
clean_y = [2 * x + 1 for x in clean_x]  # True relationship: y = 2x + 1
noisy_y = [y + random.uniform(-2, 2) for y in clean_y]  # Add noise

print("We'll compare two models:")
print("1. Simple model (appropriate complexity)")
print("2. Memorizing model (overfits)")
print()

# Simple model: learns the general trend
simple_w, simple_b = train_linear_regression(clean_x, noisy_y, learning_rate=0.01, epochs=50)

print(f"Simple model learned: y = {simple_w:.2f}x + {simple_b:.2f}")
print(f"True relationship:     y = 2.00x + 1.00")
print()

# Calculate errors
train_mse_simple = calculate_mse(clean_x, noisy_y, simple_w, simple_b)
print(f"Simple model MSE on training data: {train_mse_simple:.2f}")

# Now test on new data
test_x = [11, 12, 13]
test_y_true = [2 * x + 1 for x in test_x]
test_y_noisy = [y + random.uniform(-2, 2) for y in test_y_true]

test_mse_simple = calculate_mse(test_x, test_y_noisy, simple_w, simple_b)
print(f"Simple model MSE on test data: {test_mse_simple:.2f}")
print()

print("Notice: The simple model generalizes well to test data!")
print("It learned the pattern (y ≈ 2x + 1) rather than memorizing noise.")
print()


# ============================================================================
# SECTION 9: Feature Scaling
# ============================================================================
print("=" * 70)
print("SECTION 9: Feature Scaling (Normalization)")
print("=" * 70)
print()

# When features have different scales, it can hurt learning
raw_features = [
    [1000, 3],    # square feet, bedrooms
    [2000, 4],
    [1500, 2],
]

print("Raw features (very different scales):")
for f in raw_features:
    print(f"  Square feet: {f[0]}, Bedrooms: {f[1]}")
print()


def normalize_features(features):
    """
    Normalize each feature to 0-1 range.
    normalized = (value - min) / (max - min)
    """
    # Find min and max for each feature
    n_features = len(features[0])
    mins = [min(row[i] for row in features) for i in range(n_features)]
    maxs = [max(row[i] for row in features) for i in range(n_features)]

    # Normalize
    normalized = []
    for row in features:
        normalized_row = []
        for i, value in enumerate(row):
            if maxs[i] - mins[i] == 0:
                normalized_row.append(0)
            else:
                norm_value = (value - mins[i]) / (maxs[i] - mins[i])
                normalized_row.append(norm_value)
        normalized.append(normalized_row)

    return normalized, mins, maxs


normalized, mins, maxs = normalize_features(raw_features)

print("Normalized features (0-1 range):")
for f in normalized:
    print(f"  Square feet: {f[0]:.2f}, Bedrooms: {f[1]:.2f}")
print()
print("Now all features have similar scales, making training easier!")
print()


# ============================================================================
# SECTION 10: Complete ML Pipeline
# ============================================================================
print("=" * 70)
print("SECTION 10: Complete ML Pipeline")
print("=" * 70)
print()

print("Let's put it all together with a complete workflow!")
print()

# Step 1: Generate data
print("Step 1: Collect and prepare data")
random.seed(100)
all_sizes = [600 + i * 100 for i in range(30)]
all_prices = [80 * s + 40000 + random.uniform(-8000, 8000) for s in all_sizes]
print(f"  Generated {len(all_sizes)} house examples")

# Step 2: Split data
print()
print("Step 2: Split into train/test sets")
X_train, X_test, y_train, y_test = train_test_split(all_sizes, all_prices, test_size=0.25)
print(f"  Training: {len(X_train)} examples")
print(f"  Testing: {len(X_test)} examples")

# Step 3: Train model
print()
print("Step 3: Train the model")
final_weight, final_bias = train_linear_regression(X_train, y_train, learning_rate=0.00000001, epochs=80)

# Step 4: Evaluate
print("Step 4: Evaluate performance")
final_train_mse = calculate_mse(X_train, y_train, final_weight, final_bias)
final_test_mse = calculate_mse(X_test, y_test, final_weight, final_bias)
print(f"  Training MSE: {final_train_mse:,.0f}")
print(f"  Testing MSE: {final_test_mse:,.0f}")

# Calculate R² score (how much better than just guessing the mean)
mean_price = sum(y_test) / len(y_test)
ss_total = sum((y - mean_price) ** 2 for y in y_test)
ss_residual = sum((predict(x, final_weight, final_bias) - y) ** 2 for x, y in zip(X_test, y_test))
r_squared = 1 - (ss_residual / ss_total)
print(f"  R² score: {r_squared:.3f} (1.0 is perfect)")

# Step 5: Make predictions
print()
print("Step 5: Use model for predictions on new data")
new_houses = [1300, 2000, 2700]
print("  New house predictions:")
for size in new_houses:
    price = predict(size, final_weight, final_bias)
    print(f"    {size} sq ft -> ${price:,.0f}")

print()
print("=" * 70)
print("Pipeline complete! This is the essence of machine learning:")
print("  1. Collect data")
print("  2. Split train/test")
print("  3. Train model (learn parameters)")
print("  4. Evaluate on test data")
print("  5. Use for predictions")
print("=" * 70)
