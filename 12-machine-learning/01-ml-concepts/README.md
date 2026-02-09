# ML Concepts

## Objective

Learn what machine learning is, understand key terminology, and grasp the fundamental concepts that power modern ML systems—all without diving into complex libraries yet.

## Concepts Covered

- What is machine learning?
- Types of learning (supervised, unsupervised, reinforcement)
- Key terminology (features, labels, models, predictions)
- The ML workflow
- Overfitting and underfitting
- Train/test splits
- Common algorithms overview
- Evaluation metrics
- When to use ML vs traditional programming

## Prerequisites

- [Data Processing](../../09-data-processing/)
- Basic understanding of functions and lists
- Comfort with math concepts (means, distances)

## What is Machine Learning?

Machine learning is the science of **teaching computers to learn patterns from data** rather than explicitly programming every rule. Instead of writing code like "if temperature > 30, it's hot", you give the computer examples and let it figure out the patterns.

### Traditional Programming vs Machine Learning

**Traditional programming:**
```
Input (data) + Program (rules) → Output
```

You write explicit rules: "If email contains 'FREE!!!' and 'Click here!!!', it's spam."

**Machine learning:**
```
Input (data) + Output (labels) → Program (model)
```

You give examples of spam and not-spam emails, and the algorithm learns the patterns.

### Types of Machine Learning

#### 1. Supervised Learning

You provide **labeled data** (inputs with correct answers), and the algorithm learns to predict labels for new data.

**Examples:**
- **Regression**: Predicting continuous values (house prices, temperatures)
- **Classification**: Predicting categories (spam/not spam, cat/dog)

**Use cases:**
- Email spam detection
- House price prediction
- Medical diagnosis
- Image recognition

#### 2. Unsupervised Learning

You provide **unlabeled data**, and the algorithm finds hidden patterns or structure.

**Examples:**
- **Clustering**: Grouping similar items together
- **Dimensionality reduction**: Simplifying data while keeping important info
- **Anomaly detection**: Finding outliers

**Use cases:**
- Customer segmentation
- Recommendation systems
- Fraud detection
- Data compression

#### 3. Reinforcement Learning

An agent learns by **trial and error**, receiving rewards or penalties for actions.

**Use cases:**
- Game playing (Chess, Go)
- Robotics
- Self-driving cars
- Resource optimization

## Key Terminology

### Features (X)
The **input variables** or characteristics you use to make predictions. Also called "independent variables" or "predictors".

**Example**: To predict house prices, features might be:
- Square footage
- Number of bedrooms
- Location
- Age of the house

### Labels (y)
The **output** or **target** you're trying to predict. Also called "dependent variable" or "target variable".

**Example**: The actual house price is the label.

### Model
A mathematical function that takes features as input and produces predictions. The model has **parameters** that are adjusted during training.

Think of it as: `prediction = model(features)`

### Training
The process of **adjusting model parameters** using data so the model learns to make good predictions.

### Prediction / Inference
Using a trained model to make predictions on **new, unseen data**.

### Dataset
A collection of examples used for training or testing. Each example has features and (for supervised learning) a label.

### Hyperparameters
Settings you choose **before training** that control how the learning algorithm behaves (like learning rate, number of neighbors in k-NN).

## The Machine Learning Workflow

1. **Collect Data**: Gather relevant examples with features and labels
2. **Prepare Data**: Clean, handle missing values, normalize, split into train/test
3. **Choose Model**: Select an algorithm (linear regression, decision tree, etc.)
4. **Train Model**: Feed training data to the algorithm to learn parameters
5. **Evaluate Model**: Test performance on unseen data
6. **Tune & Iterate**: Adjust hyperparameters, try different features
7. **Deploy**: Use the model to make predictions on new data

## Training vs Testing Data

**Critical concept**: You must split your data into two sets:

### Training Set (typically 70-80% of data)
Used to train the model—the model sees these examples and learns from them.

### Testing Set (typically 20-30% of data)
Used to evaluate the model—the model has **never seen** these examples during training. This tests how well the model generalizes to new data.

**Why split?**

Imagine studying for an exam:
- If you memorize answers to practice problems but can't solve new problems, you haven't really learned
- The test set is like the real exam—it checks if you truly understand

**The golden rule**: Never let your model see the test data during training. That's cheating!

## Overfitting and Underfitting

### Underfitting
The model is **too simple** and doesn't capture the patterns in the data well. Like drawing a straight line through data that clearly curves.

**Signs**: Poor performance on both training and test data.

### Overfitting
The model is **too complex** and memorizes the training data instead of learning general patterns. It performs great on training data but poorly on test data.

**Signs**: Great performance on training data, poor performance on test data.

**Analogy**:
- Underfitting = Not studying enough for the exam
- Good fit = Understanding the concepts
- Overfitting = Memorizing answers without understanding

### How to Avoid Overfitting

- Use more training data
- Simplify your model (fewer parameters)
- Use regularization (penalize complexity)
- Use cross-validation
- Stop training early (early stopping)

## Common Algorithms Overview

### Linear Regression
Fits a straight line (or plane) to predict continuous values. Simple and interpretable.

**Use case**: Predicting house prices based on size

### Logistic Regression
Despite the name, it's used for **classification**. Predicts probabilities of categories.

**Use case**: Email is spam or not (binary classification)

### k-Nearest Neighbors (k-NN)
Classifies a point based on the majority vote of its k nearest neighbors. Simple but powerful.

**Use case**: Handwritten digit recognition

### Decision Trees
Makes decisions by asking a series of yes/no questions. Easy to understand and visualize.

**Use case**: Loan approval decisions

### K-Means Clustering
Groups data into k clusters based on similarity.

**Use case**: Customer segmentation

### Neural Networks
Inspired by the brain, chains together many simple calculations to learn complex patterns.

**Use case**: Image recognition, language translation

## Evaluation Metrics

### For Regression (predicting numbers)

**Mean Squared Error (MSE)**
```
MSE = average of (predicted - actual)²
```
Lower is better. Heavily penalizes large errors.

**Mean Absolute Error (MAE)**
```
MAE = average of |predicted - actual|
```
Lower is better. Treats all errors equally.

**R² Score (Coefficient of Determination)**
```
R² measures how well predictions fit the data (0 to 1)
```
Higher is better. 1 = perfect fit, 0 = as good as guessing the mean.

### For Classification (predicting categories)

**Accuracy**
```
Accuracy = (correct predictions) / (total predictions)
```
Simple but can be misleading with imbalanced data.

**Precision**
```
Precision = true positives / (true positives + false positives)
```
Of the items we predicted as positive, how many were actually positive?

**Recall (Sensitivity)**
```
Recall = true positives / (true positives + false negatives)
```
Of all the actual positive items, how many did we find?

**F1 Score**
```
F1 = 2 × (precision × recall) / (precision + recall)
```
Harmonic mean of precision and recall.

## When to Use ML vs Traditional Programming

### Use Machine Learning When:

✅ The problem has **patterns** but no clear rules
- "What makes an email spam?" - Hard to define explicitly

✅ You have **lots of data** with examples
- Thousands of labeled emails

✅ The problem is **too complex** for manual rules
- Image recognition: millions of pixel combinations

✅ The rules **change over time**
- Spam patterns evolve constantly

✅ You need to **handle variations** and edge cases
- Recognizing cats: many breeds, angles, lighting conditions

### Use Traditional Programming When:

✅ You have **clear, fixed rules**
- Calculate tax based on income brackets

✅ You have **little or no data**
- Business logic for a new system

✅ You need **100% predictability**
- Banking transactions must follow exact rules

✅ The solution is **simple and well-defined**
- Sort a list, calculate an average

✅ **Interpretability is critical**
- Legal or medical decisions requiring explanation

## Feature Engineering

The features you choose are often **more important** than the algorithm you use. Good features make learning easier.

**Examples of feature engineering:**
- **Creating new features**: From a date, extract day of week, month, season
- **Combining features**: Multiply bedroom count by square footage
- **Transforming features**: Take log of prices, convert text to word counts
- **Scaling features**: Normalize values to 0-1 range or standardize

## The Bias-Variance Tradeoff

**Bias**: Error from wrong assumptions (oversimplifying). High bias → underfitting.

**Variance**: Error from sensitivity to small fluctuations in training data. High variance → overfitting.

**Goal**: Find the sweet spot—low bias and low variance.

## Key Takeaways

1. **Machine learning finds patterns in data** instead of following explicit rules
2. **Training data teaches**, test data evaluates—never mix them
3. **Features (X) are inputs**, labels (y) are outputs you want to predict
4. **Overfitting is memorizing**, underfitting is failing to learn
5. **The right features matter** as much as the right algorithm
6. **Evaluation metrics tell you** how well your model performs
7. **ML is powerful but not always the answer**—know when traditional programming is better

## What's Next?

In the following lessons, you'll:
- Implement linear regression from scratch
- Build classification models
- Work with real datasets
- Use popular ML libraries (scikit-learn)
- Build neural networks
- Deploy ML models

But first, you need to understand these fundamental concepts—they're the foundation everything else builds on!

## Code Example

Check out [`example.py`](example.py) for a complete working example implementing basic ML concepts from scratch.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.
