# scikit-learn Basics

## Objective

Learn the fundamentals of scikit-learn, Python's most popular machine learning library, and build your first ML models.

## Concepts Covered

- The scikit-learn API pattern (fit, predict, score)
- Train/test split for model evaluation
- Linear Regression for predicting continuous values
- Classification models (Logistic Regression, Decision Trees)
- Data preprocessing (scaling, encoding)
- Model evaluation metrics (accuracy, MSE, confusion matrix)
- Cross-validation for robust evaluation
- Pipelines for cleaner workflows

## Prerequisites

- [ML Concepts](../01-ml-concepts/)
- [NumPy Basics](../../09-data-processing/01-numpy-basics/)

## What is scikit-learn?

scikit-learn (often imported as `sklearn`) is the go-to library for machine learning in Python. It provides:

- **Simple, consistent API** — almost every model uses the same pattern
- **Wide variety of algorithms** — regression, classification, clustering, and more
- **Built-in preprocessing tools** — scaling, encoding, feature engineering
- **Model evaluation utilities** — metrics, cross-validation, grid search
- **Excellent documentation** — clear examples and explanations

The beauty of scikit-learn is that once you learn the pattern for one model, you can apply it to dozens of others.

## The scikit-learn API Pattern

Every scikit-learn model follows the same workflow:

```python
# 1. Create the model
model = SomeModel()

# 2. Train it on data
model.fit(X_train, y_train)

# 3. Make predictions
predictions = model.predict(X_test)

# 4. Evaluate performance
score = model.score(X_test, y_test)
```

This consistency makes it easy to experiment with different algorithms.

## Train/Test Split

To evaluate how well a model generalizes to new data, we split our dataset:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 80% for training, 20% for testing
```

The `random_state` parameter ensures reproducibility.

## Regression: Predicting Continuous Values

**Linear Regression** finds the best-fit line through your data:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# R² score (1.0 is perfect)
score = model.score(X_test, y_test)
```

Common metrics:
- **R² score** — how much variance the model explains (0 to 1, higher is better)
- **Mean Squared Error (MSE)** — average squared difference between predictions and actual values (lower is better)
- **Mean Absolute Error (MAE)** — average absolute difference (lower is better)

## Classification: Predicting Categories

**Logistic Regression** (despite the name, it's for classification):

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Accuracy score
accuracy = model.score(X_test, y_test)
```

**Decision Trees** — intuitive, interpretable models:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)
```

Common metrics:
- **Accuracy** — percentage of correct predictions
- **Confusion Matrix** — shows true positives, false positives, etc.
- **Precision, Recall, F1-score** — for imbalanced datasets

## Data Preprocessing

Most models need properly scaled data:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same scaling!
```

**Important**: Always fit the scaler on training data only, then apply to both train and test.

## Model Evaluation

```python
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix

# For regression
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

# For classification
accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
```

## Cross-Validation

Instead of a single train/test split, cross-validation tests the model multiple times:

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)  # 5-fold CV
print(f"Mean accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

This gives a more reliable estimate of model performance.

## Pipelines

Pipelines combine preprocessing and modeling into one step:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

Benefits:
- Cleaner code
- Prevents data leakage
- Easy to deploy

## Common Pitfalls

1. **Forgetting to split data** — always evaluate on unseen test data
2. **Scaling test data incorrectly** — fit scaler on training data only
3. **Overfitting** — model memorizes training data but fails on new data
4. **Ignoring data preprocessing** — most models need scaled/normalized features
5. **Using wrong metrics** — accuracy can be misleading for imbalanced datasets

## Quick Reference

```python
# Regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Preprocessing
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Evaluation
from sklearn.model_selection import cross_val_score
```

## Next Steps

After mastering these basics, explore:
- Random Forests and ensemble methods
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Model tuning with GridSearchCV
- Feature selection and engineering
- Handling imbalanced datasets

## Code Example

Check out [`example.py`](example.py) for a complete working example.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.
