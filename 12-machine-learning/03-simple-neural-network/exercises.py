"""
Simple Neural Network — Exercises
==================================

Practice problems to test your understanding.
Try to solve each exercise before looking at the solutions below.
"""

import math
import random


# =============================================================================
# Exercise 1: Implement a dot product function
# Calculate the dot product of two vectors (sum of element-wise products).
# Example: dot_product([1, 2, 3], [4, 5, 6]) = 1*4 + 2*5 + 3*6 = 32
# =============================================================================

def exercise_1():
    """Implement dot product manually."""
    print("Implement a function that calculates the dot product of two vectors.")
    print("Don't use any libraries - just loops and basic math!\n")

    def dot_product(vec1, vec2):
        # TODO: Implement this
        return None  # Replace this with your implementation

    # Test it
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = dot_product(a, b)
    print(f"dot_product({a}, {b}) = {result}")
    print(f"Expected: 32")
    print("\n(Implement the function to see the correct result)")


# =============================================================================
# Exercise 2: Implement activation functions
# Create sigmoid and ReLU activation functions from scratch.
# sigmoid(x) = 1 / (1 + e^(-x))
# relu(x) = max(0, x)
# =============================================================================

def exercise_2():
    """Implement sigmoid and ReLU activation functions."""
    print("Implement sigmoid and ReLU activation functions.\n")

    def sigmoid(x):
        # TODO: Implement sigmoid
        return None  # Replace this with your implementation

    def relu(x):
        # TODO: Implement ReLU
        return None  # Replace this with your implementation

    # Test them
    test_values = [-2, -1, 0, 1, 2]
    print("Testing sigmoid:")
    for val in test_values:
        result = sigmoid(val)
        print(f"  sigmoid({val}) = {result if result is not None else 'TODO'}")

    print("\nTesting ReLU:")
    for val in test_values:
        result = relu(val)
        print(f"  relu({val}) = {result if result is not None else 'TODO'}")


# =============================================================================
# Exercise 3: Create a simple neuron
# Build a Neuron class with:
# - Random weight initialization
# - A forward method that computes: sigmoid(sum(inputs * weights) + bias)
# =============================================================================

def exercise_3():
    """Create a simple neuron class."""
    print("Create a Neuron class that can make predictions.\n")

    class Neuron:
        def __init__(self, num_inputs):
            # TODO: Initialize random weights and bias
            pass

        def forward(self, inputs):
            # TODO: Compute weighted sum + bias, apply sigmoid
            return None  # Replace this with your implementation

    # Test it
    neuron = Neuron(num_inputs=3)
    result = neuron.forward([0.5, 0.3, 0.8])
    print(f"Neuron output: {result if result is not None else 'TODO - implement the class'}")
    print("(Your output will vary due to random weights)")


# =============================================================================
# Exercise 4: Calculate Mean Squared Error (MSE)
# MSE measures how wrong predictions are.
# MSE = average of (prediction - actual)^2 for all examples
# =============================================================================

def exercise_4():
    """Calculate mean squared error."""
    print("Implement MSE loss function.\n")

    def mse_loss(predictions, targets):
        # TODO: Calculate mean squared error
        return None  # Replace this with your implementation

    # Test it
    predictions = [0.8, 0.2, 0.9, 0.1]
    targets = [1, 0, 1, 0]
    loss = mse_loss(predictions, targets)
    print(f"Predictions: {predictions}")
    print(f"Targets: {targets}")
    print(f"MSE Loss: {loss if loss is not None else 'TODO'}")
    print(f"Expected: 0.0175")


# =============================================================================
# Exercise 5: Implement the sigmoid derivative
# The derivative of sigmoid(x) = sigmoid(x) * (1 - sigmoid(x))
# This is used in backpropagation to calculate gradients.
# =============================================================================

def exercise_5():
    """Implement sigmoid derivative."""
    print("Implement the derivative of the sigmoid function.\n")

    def sigmoid(x):
        try:
            return 1 / (1 + math.exp(-x))
        except OverflowError:
            return 0.0 if x < 0 else 1.0

    def sigmoid_derivative(x):
        # TODO: Implement sigmoid derivative
        # Hint: sigmoid'(x) = sigmoid(x) * (1 - sigmoid(x))
        return None  # Replace this with your implementation

    # Test it
    test_values = [-2, -1, 0, 1, 2]
    print("sigmoid'(x) should be highest at x=0 and approach 0 at extremes:\n")
    for val in test_values:
        deriv = sigmoid_derivative(val)
        if deriv is not None:
            print(f"  sigmoid'({val:2}) = {deriv:.4f}")
        else:
            print(f"  sigmoid'({val:2}) = TODO")


# =============================================================================
# Exercise 6: Train a perceptron on OR gate
# Train a single neuron to learn the OR logic gate.
# OR gate: 0 OR 0 = 0, 0 OR 1 = 1, 1 OR 0 = 1, 1 OR 1 = 1
# =============================================================================

def exercise_6():
    """Train a perceptron to learn OR gate."""
    print("Train a perceptron to learn the OR logic gate.\n")

    class Neuron:
        def __init__(self, num_inputs):
            self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
            self.bias = random.uniform(-1, 1)

        def forward(self, inputs):
            weighted_sum = sum(i * w for i, w in zip(inputs, self.weights))
            weighted_sum += self.bias
            return self.sigmoid(weighted_sum)

        @staticmethod
        def sigmoid(x):
            try:
                return 1 / (1 + math.exp(-x))
            except OverflowError:
                return 0.0 if x < 0 else 1.0

    # OR gate training data
    or_data = [
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 1),
    ]

    print("Target OR gate:")
    for inputs, target in or_data:
        print(f"  {inputs[0]} OR {inputs[1]} = {target}")

    # TODO: Train the neuron
    # Hint: Use the same training approach as in the example
    # For each epoch:
    #   For each training example:
    #     1. Forward pass: get prediction
    #     2. Calculate error: target - prediction
    #     3. Update weights: weight += learning_rate * error * input * output * (1 - output)
    #     4. Update bias: bias += learning_rate * error * output * (1 - output)

    neuron = Neuron(num_inputs=2)
    learning_rate = 1.0
    epochs = 1000

    print("\nTODO: Implement training loop here\n")

    # Test the trained neuron
    print("Testing trained OR gate:")
    for inputs, expected in or_data:
        output = neuron.forward(inputs)
        predicted = 1 if output > 0.5 else 0
        print(f"  {inputs[0]} OR {inputs[1]} = {predicted} (output: {output:.4f})")


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    """Solution: Dot product."""
    print("SOLUTION: Dot product\n")

    def dot_product(vec1, vec2):
        """Calculate dot product of two vectors."""
        if len(vec1) != len(vec2):
            raise ValueError("Vectors must have same length")
        return sum(a * b for a, b in zip(vec1, vec2))

    # Test it
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = dot_product(a, b)
    print(f"dot_product({a}, {b}) = {result}")
    print(f"Expected: 32")
    print(f"Correct: {result == 32}")


def solution_2():
    """Solution: Activation functions."""
    print("SOLUTION: Activation functions\n")

    def sigmoid(x):
        """Sigmoid activation function."""
        try:
            return 1 / (1 + math.exp(-x))
        except OverflowError:
            return 0.0 if x < 0 else 1.0

    def relu(x):
        """ReLU activation function."""
        return max(0, x)

    # Test them
    test_values = [-2, -1, 0, 1, 2]
    print("Testing sigmoid:")
    for val in test_values:
        print(f"  sigmoid({val:2}) = {sigmoid(val):.4f}")

    print("\nTesting ReLU:")
    for val in test_values:
        print(f"  relu({val:2}) = {relu(val):.4f}")


def solution_3():
    """Solution: Simple neuron class."""
    print("SOLUTION: Simple neuron class\n")

    class Neuron:
        def __init__(self, num_inputs):
            # Initialize random weights and bias
            self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
            self.bias = random.uniform(-1, 1)

        def forward(self, inputs):
            # Compute weighted sum
            weighted_sum = sum(i * w for i, w in zip(inputs, self.weights))
            weighted_sum += self.bias

            # Apply sigmoid activation
            return self.sigmoid(weighted_sum)

        @staticmethod
        def sigmoid(x):
            try:
                return 1 / (1 + math.exp(-x))
            except OverflowError:
                return 0.0 if x < 0 else 1.0

    # Test it
    neuron = Neuron(num_inputs=3)
    result = neuron.forward([0.5, 0.3, 0.8])
    print(f"Neuron weights: {[f'{w:.3f}' for w in neuron.weights]}")
    print(f"Neuron bias: {neuron.bias:.3f}")
    print(f"Neuron output: {result:.4f}")


def solution_4():
    """Solution: MSE loss."""
    print("SOLUTION: Mean Squared Error\n")

    def mse_loss(predictions, targets):
        """Calculate mean squared error."""
        if len(predictions) != len(targets):
            raise ValueError("Predictions and targets must have same length")

        squared_errors = [(pred - target) ** 2
                         for pred, target in zip(predictions, targets)]
        return sum(squared_errors) / len(squared_errors)

    # Test it
    predictions = [0.8, 0.2, 0.9, 0.1]
    targets = [1, 0, 1, 0]
    loss = mse_loss(predictions, targets)
    print(f"Predictions: {predictions}")
    print(f"Targets: {targets}")
    print(f"MSE Loss: {loss:.4f}")
    print(f"Expected: 0.0175")


def solution_5():
    """Solution: Sigmoid derivative."""
    print("SOLUTION: Sigmoid derivative\n")

    def sigmoid(x):
        try:
            return 1 / (1 + math.exp(-x))
        except OverflowError:
            return 0.0 if x < 0 else 1.0

    def sigmoid_derivative(x):
        """Derivative of sigmoid function."""
        s = sigmoid(x)
        return s * (1 - s)

    # Test it
    test_values = [-2, -1, 0, 1, 2]
    print("Sigmoid derivative (highest at x=0, approaches 0 at extremes):\n")
    for val in test_values:
        sig = sigmoid(val)
        deriv = sigmoid_derivative(val)
        print(f"  x={val:2}: sigmoid={sig:.4f}, sigmoid'={deriv:.4f}")


def solution_6():
    """Solution: Train OR gate."""
    print("SOLUTION: Train OR gate\n")

    class Neuron:
        def __init__(self, num_inputs):
            self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
            self.bias = random.uniform(-1, 1)

        def forward(self, inputs):
            weighted_sum = sum(i * w for i, w in zip(inputs, self.weights))
            weighted_sum += self.bias
            return self.sigmoid(weighted_sum)

        @staticmethod
        def sigmoid(x):
            try:
                return 1 / (1 + math.exp(-x))
            except OverflowError:
                return 0.0 if x < 0 else 1.0

    # OR gate training data
    or_data = [
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 1),
    ]

    print("Target OR gate:")
    for inputs, target in or_data:
        print(f"  {inputs[0]} OR {inputs[1]} = {target}")

    # Train the neuron
    neuron = Neuron(num_inputs=2)
    learning_rate = 1.0
    epochs = 1000

    print("\nTraining...")
    for epoch in range(epochs):
        total_error = 0

        for inputs, target in or_data:
            # Forward pass
            output = neuron.forward(inputs)

            # Calculate error
            error = target - output
            total_error += error ** 2

            # Update weights and bias
            for i in range(len(neuron.weights)):
                neuron.weights[i] += learning_rate * error * inputs[i] * output * (1 - output)
            neuron.bias += learning_rate * error * output * (1 - output)

        # Print progress
        if epoch % 200 == 0:
            avg_error = total_error / len(or_data)
            print(f"  Epoch {epoch:4}: Average error = {avg_error:.6f}")

    # Test the trained neuron
    print("\nTesting trained OR gate:")
    for inputs, expected in or_data:
        output = neuron.forward(inputs)
        predicted = 1 if output > 0.5 else 0
        status = "✓" if predicted == expected else "✗"
        print(f"  {inputs[0]} OR {inputs[1]} = {predicted} (output: {output:.4f}, expected: {expected}) {status}")


# =============================================================================
# Runner
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Implement dot product", exercise_1),
        ("Implement activation functions", exercise_2),
        ("Create a simple neuron", exercise_3),
        ("Calculate MSE loss", exercise_4),
        ("Implement sigmoid derivative", exercise_5),
        ("Train a perceptron on OR gate", exercise_6),
    ]

    solutions = [
        ("Dot product", solution_1),
        ("Activation functions", solution_2),
        ("Simple neuron class", solution_3),
        ("MSE loss", solution_4),
        ("Sigmoid derivative", solution_5),
        ("Train OR gate", solution_6),
    ]

    print("=" * 70)
    print("SIMPLE NEURAL NETWORK — EXERCISES")
    print("=" * 70)
    print("\nTry each exercise before looking at the solutions!\n")

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 70)
        print(f"EXERCISE {i}: {title}")
        print("=" * 70)
        func()
        print()

    # Ask if user wants to see solutions
    print("\n" + "=" * 70)
    print("SOLUTIONS")
    print("=" * 70)
    print("\nHere are the solutions for reference:\n")

    for i, (title, func) in enumerate(solutions, 1):
        print("=" * 70)
        print(f"SOLUTION {i}: {title}")
        print("=" * 70)
        func()
        print()

    print("=" * 70)
    print("Great job! You've learned the building blocks of neural networks!")
    print("=" * 70)
