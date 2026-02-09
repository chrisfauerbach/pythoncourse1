# Simple Neural Network

Neural networks are one of the coolest ideas in machine learning. They're inspired by how brains work (kind of), and they can learn to recognize patterns, make predictions, and solve problems that traditional programming struggles with.

In this lesson, we'll build a neural network **from scratch** using only Python's standard library. No TensorFlow, no PyTorch — just pure Python. This way, you'll understand what's actually happening under the hood.

## What is a Neural Network?

Think of a neural network as a collection of connected "neurons" organized in layers:

- **Input layer**: receives your data (features)
- **Hidden layer(s)**: processes and transforms the data
- **Output layer**: produces predictions or classifications

Each connection between neurons has a **weight** (how strong the connection is), and each neuron has a **bias** (a threshold for activation). The network learns by adjusting these weights and biases.

## The Perceptron: The Simplest Neural Unit

A perceptron is the building block of neural networks. Here's what it does:

1. Takes multiple inputs (x₁, x₂, x₃, ...)
2. Multiplies each input by a weight (w₁, w₂, w₃, ...)
3. Adds a bias term (b)
4. Passes the result through an activation function
5. Outputs a single value

The formula: `output = activation(w₁×x₁ + w₂×x₂ + ... + b)`

## Activation Functions

Activation functions add non-linearity to the network. Without them, stacking layers would be pointless — it would just be linear algebra!

**Common activation functions:**

- **Step function**: outputs 0 or 1 (binary, used in simple perceptrons)
- **Sigmoid**: smooth S-curve, outputs between 0 and 1 (good for probabilities)
- **ReLU (Rectified Linear Unit)**: outputs max(0, x) (simple, fast, popular)
- **Tanh**: similar to sigmoid but outputs between -1 and 1

```python
# Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# ReLU
def relu(x):
    return max(0, x)

# Step function
def step(x):
    return 1 if x >= 0 else 0
```

## Forward Propagation

Forward propagation is how data flows through the network:

1. Start with input values
2. For each layer:
   - Compute weighted sum of inputs + bias
   - Apply activation function
   - Pass outputs to next layer
3. Get final prediction from output layer

This is the "thinking" part of the network — making predictions based on current weights.

## Loss Functions

The loss function measures how wrong the network's predictions are. Common ones:

- **Mean Squared Error (MSE)**: average of (prediction - actual)² — good for regression
- **Binary Cross-Entropy**: for binary classification (0 or 1)
- **Categorical Cross-Entropy**: for multi-class classification

Lower loss = better predictions!

## Backpropagation: How Networks Learn

Backpropagation is the magic behind neural networks. It calculates how much each weight contributed to the error, then adjusts weights to reduce that error.

**The process:**

1. Compute loss (how wrong was the prediction?)
2. Calculate gradients (how should we change each weight?)
3. Update weights in the direction that reduces loss
4. Use a learning rate to control step size

This uses calculus (chain rule) behind the scenes, but conceptually: "If increasing this weight increases the error, decrease the weight. If increasing it decreases the error, increase the weight."

## The Training Loop

Training a neural network follows this pattern:

```python
for epoch in range(num_epochs):
    for input_data, target in training_data:
        # 1. Forward pass: make a prediction
        prediction = network.forward(input_data)

        # 2. Calculate loss: how wrong were we?
        loss = calculate_loss(prediction, target)

        # 3. Backward pass: compute gradients
        gradients = network.backward(loss)

        # 4. Update weights: learn from mistakes
        network.update_weights(gradients, learning_rate)
```

Over many epochs (iterations through the data), the network gets better and better!

## Neural Networks vs. Simpler Models

**Use neural networks when:**
- You have lots of data (they need it to learn)
- Relationships are complex and non-linear
- Features interact in complicated ways
- You're working with images, audio, text, or sequences

**Use simpler models (linear/logistic regression, decision trees) when:**
- You have limited data
- You need to explain your model's decisions
- Relationships are mostly linear
- Speed and simplicity matter more than accuracy

Neural networks are powerful but not always the best tool. Start simple, add complexity only when needed.

## The XOR Problem

XOR (exclusive OR) is the classic neural network demo. It's a function that outputs 1 when inputs are different, 0 when they're the same:

```
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
```

This is impossible for a single perceptron to learn (it's not linearly separable), but a 2-layer network can solve it! This shows why hidden layers are important.

## Key Takeaways

1. Neural networks learn by adjusting weights through backpropagation
2. Activation functions provide non-linearity (essential for complex patterns)
3. Training involves: forward pass → loss calculation → backward pass → weight update
4. Hidden layers let networks learn complex, non-linear relationships
5. More layers/neurons ≠ always better (can overfit!)
6. Learning rate matters: too high = unstable, too low = slow learning

## What's Next?

This lesson shows the fundamentals from scratch. In practice, you'd use libraries like PyTorch or TensorFlow that:
- Handle the calculus automatically (autograd)
- Run on GPUs for speed
- Provide optimized implementations
- Offer pre-built layers and architectures

But understanding the basics helps you debug issues, tune hyperparameters, and design better architectures!

---

**Files in this lesson:**
- `example.py` — complete neural network implementation from scratch
- `exercises.py` — hands-on practice building components

Run the example to see a neural network learn XOR from scratch!
