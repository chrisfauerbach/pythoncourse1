"""
Simple Neural Network — Example Code
======================================

Building a neural network from scratch using only Python stdlib + math module.
This demonstrates the core concepts: neurons, forward propagation, backpropagation,
and training.

Run this file:
    python3 example.py
"""

import math
import random


# =============================================================================
# ACTIVATION FUNCTIONS
# =============================================================================

def sigmoid(x):
    """Sigmoid activation: outputs between 0 and 1, smooth S-curve."""
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        # Handle extreme values
        return 0.0 if x < 0 else 1.0


def sigmoid_derivative(x):
    """Derivative of sigmoid, used in backpropagation."""
    s = sigmoid(x)
    return s * (1 - s)


def relu(x):
    """ReLU activation: max(0, x) — simple and effective."""
    return max(0, x)


def relu_derivative(x):
    """Derivative of ReLU."""
    return 1 if x > 0 else 0


def step_function(x):
    """Step function: outputs 0 or 1 (used in classic perceptrons)."""
    return 1 if x >= 0 else 0


print("ACTIVATION FUNCTIONS")
print("=" * 60)
print("\nSigmoid (smooth, 0 to 1):")
for val in [-2, -1, 0, 1, 2]:
    print(f"  sigmoid({val:2}) = {sigmoid(val):.4f}")

print("\nReLU (max(0, x)):")
for val in [-2, -1, 0, 1, 2]:
    print(f"  relu({val:2}) = {relu(val):.4f}")

print("\nStep function (binary):")
for val in [-2, -1, 0, 1, 2]:
    print(f"  step({val:2}) = {step_function(val)}")


# =============================================================================
# SINGLE NEURON / PERCEPTRON
# =============================================================================

print("\n\nSINGLE NEURON")
print("=" * 60)

class Neuron:
    """A single neuron with weights, bias, and activation function."""

    def __init__(self, num_inputs):
        # Initialize weights randomly between -1 and 1
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        self.bias = random.uniform(-1, 1)

    def forward(self, inputs):
        """Forward pass: compute weighted sum + bias, then apply activation."""
        # Dot product: sum of (input * weight)
        weighted_sum = sum(i * w for i, w in zip(inputs, self.weights))
        weighted_sum += self.bias

        # Apply sigmoid activation
        output = sigmoid(weighted_sum)
        return output

    def __repr__(self):
        return f"Neuron(weights={[f'{w:.3f}' for w in self.weights]}, bias={self.bias:.3f})"


# Create a neuron with 2 inputs
neuron = Neuron(num_inputs=2)
print(f"Created: {neuron}")

# Test it with some inputs
test_inputs = [0.5, 0.8]
output = neuron.forward(test_inputs)
print(f"\nInput: {test_inputs}")
print(f"Output: {output:.4f}")


# =============================================================================
# TRAINING A PERCEPTRON (AND GATE)
# =============================================================================

print("\n\nTRAINING A PERCEPTRON: AND GATE")
print("=" * 60)

# AND gate truth table
and_data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1),
]

print("\nTarget function (AND gate):")
for inputs, target in and_data:
    print(f"  {inputs[0]} AND {inputs[1]} = {target}")


def train_perceptron(neuron, training_data, learning_rate=0.5, epochs=1000):
    """Train a single neuron using gradient descent."""
    for epoch in range(epochs):
        total_error = 0

        for inputs, target in training_data:
            # Forward pass
            output = neuron.forward(inputs)

            # Calculate error
            error = target - output
            total_error += error ** 2

            # Update weights and bias (simplified gradient descent)
            # This is a basic update rule for demonstration
            for i in range(len(neuron.weights)):
                neuron.weights[i] += learning_rate * error * inputs[i] * output * (1 - output)
            neuron.bias += learning_rate * error * output * (1 - output)

        # Print progress every 200 epochs
        if epoch % 200 == 0 or epoch == epochs - 1:
            avg_error = total_error / len(training_data)
            print(f"  Epoch {epoch:4}: Average error = {avg_error:.6f}")


# Train the neuron
and_neuron = Neuron(num_inputs=2)
train_perceptron(and_neuron, and_data, learning_rate=1.0, epochs=1000)

print("\nTesting trained AND gate:")
for inputs, expected in and_data:
    output = and_neuron.forward(inputs)
    predicted = 1 if output > 0.5 else 0
    print(f"  {inputs[0]} AND {inputs[1]} = {predicted} (output: {output:.4f}, expected: {expected})")


# =============================================================================
# SIMPLE 2-LAYER NEURAL NETWORK CLASS
# =============================================================================

print("\n\n2-LAYER NEURAL NETWORK")
print("=" * 60)

class NeuralNetwork:
    """A simple 2-layer neural network (input -> hidden -> output)."""

    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights randomly (small values work better)
        # Hidden layer weights: [hidden_size x input_size]
        self.weights_input_hidden = [
            [random.uniform(-1, 1) for _ in range(input_size)]
            for _ in range(hidden_size)
        ]
        self.bias_hidden = [random.uniform(-1, 1) for _ in range(hidden_size)]

        # Output layer weights: [output_size x hidden_size]
        self.weights_hidden_output = [
            [random.uniform(-1, 1) for _ in range(hidden_size)]
            for _ in range(output_size)
        ]
        self.bias_output = [random.uniform(-1, 1) for _ in range(output_size)]

        # Storage for intermediate values (needed for backpropagation)
        self.hidden_inputs = []
        self.hidden_outputs = []
        self.output_inputs = []
        self.output_outputs = []

    def forward(self, inputs):
        """Forward propagation through the network."""
        # Hidden layer
        self.hidden_inputs = []
        self.hidden_outputs = []

        for i in range(self.hidden_size):
            # Weighted sum for this hidden neuron
            weighted_sum = sum(inputs[j] * self.weights_input_hidden[i][j]
                             for j in range(self.input_size))
            weighted_sum += self.bias_hidden[i]
            self.hidden_inputs.append(weighted_sum)

            # Apply activation
            activated = sigmoid(weighted_sum)
            self.hidden_outputs.append(activated)

        # Output layer
        self.output_inputs = []
        self.output_outputs = []

        for i in range(self.output_size):
            # Weighted sum for this output neuron
            weighted_sum = sum(self.hidden_outputs[j] * self.weights_hidden_output[i][j]
                             for j in range(self.hidden_size))
            weighted_sum += self.bias_output[i]
            self.output_inputs.append(weighted_sum)

            # Apply activation
            activated = sigmoid(weighted_sum)
            self.output_outputs.append(activated)

        return self.output_outputs

    def backward(self, inputs, targets, learning_rate):
        """Backpropagation: calculate gradients and update weights."""
        # Calculate output layer errors
        output_errors = []
        for i in range(self.output_size):
            error = targets[i] - self.output_outputs[i]
            output_errors.append(error)

        # Calculate output layer deltas (error * derivative)
        output_deltas = []
        for i in range(self.output_size):
            delta = output_errors[i] * sigmoid_derivative(self.output_inputs[i])
            output_deltas.append(delta)

        # Calculate hidden layer errors (backpropagate from output)
        hidden_errors = []
        for i in range(self.hidden_size):
            error = sum(output_deltas[j] * self.weights_hidden_output[j][i]
                       for j in range(self.output_size))
            hidden_errors.append(error)

        # Calculate hidden layer deltas
        hidden_deltas = []
        for i in range(self.hidden_size):
            delta = hidden_errors[i] * sigmoid_derivative(self.hidden_inputs[i])
            hidden_deltas.append(delta)

        # Update output layer weights
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                self.weights_hidden_output[i][j] += learning_rate * output_deltas[i] * self.hidden_outputs[j]
            self.bias_output[i] += learning_rate * output_deltas[i]

        # Update hidden layer weights
        for i in range(self.hidden_size):
            for j in range(self.input_size):
                self.weights_input_hidden[i][j] += learning_rate * hidden_deltas[i] * inputs[j]
            self.bias_hidden[i] += learning_rate * hidden_deltas[i]

        # Return total error for monitoring
        return sum(e ** 2 for e in output_errors)


print("\nCreated network: 2 inputs -> 4 hidden -> 1 output")
network = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)


# =============================================================================
# TRAINING ON XOR (THE CLASSIC DEMO)
# =============================================================================

print("\n\nTRAINING ON XOR PROBLEM")
print("=" * 60)

# XOR truth table (impossible for single perceptron!)
xor_data = [
    ([0, 0], [0]),
    ([0, 1], [1]),
    ([1, 0], [1]),
    ([1, 1], [0]),
]

print("\nTarget function (XOR gate):")
for inputs, target in xor_data:
    print(f"  {inputs[0]} XOR {inputs[1]} = {target[0]}")

print("\nTraining...")
learning_rate = 0.5
epochs = 5000
loss_history = []

for epoch in range(epochs):
    total_loss = 0

    # Train on each example
    for inputs, targets in xor_data:
        # Forward pass
        outputs = network.forward(inputs)

        # Backward pass and weight update
        loss = network.backward(inputs, targets, learning_rate)
        total_loss += loss

    # Track average loss
    avg_loss = total_loss / len(xor_data)
    loss_history.append(avg_loss)

    # Print progress
    if epoch % 1000 == 0 or epoch == epochs - 1:
        print(f"  Epoch {epoch:5}: Loss = {avg_loss:.6f}")

print("\nTesting trained XOR network:")
for inputs, expected in xor_data:
    outputs = network.forward(inputs)
    predicted = 1 if outputs[0] > 0.5 else 0
    print(f"  {inputs[0]} XOR {inputs[1]} = {predicted} (output: {outputs[0]:.4f}, expected: {expected[0]})")


# =============================================================================
# VISUALIZING TRAINING PROGRESS
# =============================================================================

print("\n\nTRAINING PROGRESS VISUALIZATION")
print("=" * 60)

def plot_loss_ascii(loss_history, width=60, height=15):
    """Create an ASCII chart of loss over time."""
    if not loss_history:
        return

    max_loss = max(loss_history)
    min_loss = min(loss_history)
    loss_range = max_loss - min_loss if max_loss != min_loss else 1

    # Sample the loss history to fit the width
    step = max(1, len(loss_history) // width)
    sampled = [loss_history[i] for i in range(0, len(loss_history), step)]

    print(f"\nLoss over time (from {max_loss:.4f} to {min_loss:.4f}):\n")

    # Draw chart from top to bottom
    for row in range(height):
        # Calculate threshold for this row
        threshold = max_loss - (row / height) * loss_range

        # Draw the row
        line = ""
        for loss in sampled:
            if loss >= threshold:
                line += "█"
            else:
                line += " "

        # Add Y-axis label
        if row == 0:
            print(f"{max_loss:6.4f} |{line}|")
        elif row == height - 1:
            print(f"{min_loss:6.4f} |{line}|")
        else:
            print(f"       |{line}|")

    # X-axis
    print(f"       +{'-' * len(sampled)}+")
    print(f"        0{' ' * (len(sampled) - 10)}epochs={len(loss_history)}")


plot_loss_ascii(loss_history)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n\nKEY TAKEAWAYS")
print("=" * 60)
print("""
1. Neural networks are made of layers of neurons, each with weights and biases

2. Activation functions (sigmoid, ReLU) add non-linearity, enabling complex patterns

3. Forward propagation: data flows through layers to produce output

4. Loss measures how wrong predictions are (lower is better)

5. Backpropagation calculates how to adjust weights to reduce loss

6. Training loop: forward → loss → backward → update weights → repeat

7. Hidden layers are essential for non-linear problems like XOR

8. Learning rate controls how fast the network learns (tune carefully!)

The XOR problem proves why hidden layers matter: a single perceptron can't
solve it, but a 2-layer network learns it perfectly!

In practice, use frameworks like PyTorch or TensorFlow, but understanding
these fundamentals helps you debug, tune, and design better architectures.
""")
