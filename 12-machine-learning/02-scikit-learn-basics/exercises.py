"""
scikit-learn Basics — Exercises
================================

Practice problems to test your understanding of scikit-learn fundamentals.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import sys

try:
    import numpy as np
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn.pipeline import Pipeline
    from sklearn.datasets import make_classification
except ImportError:
    print("This lesson requires scikit-learn and numpy.")
    print("Install them with: pip install scikit-learn numpy")
    print("Then try again!")
    sys.exit(0)


# =============================================================================
# Exercise 1: Train your first model
#
# Given these arrays representing hours studied vs exam scores:
#   hours = np.array([[1], [2], [3], [4], [5], [6]])
#   scores = np.array([50, 55, 65, 70, 80, 90])
#
# Tasks:
#   a) Create a LinearRegression model
#   b) Fit it on the data
#   c) Print the model's coefficient and intercept
#   d) Predict the score for someone who studies 7 hours
#   e) Calculate and print the R² score
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Train/test split
#
# Create a regression dataset using:
#   X, y = make_regression(n_samples=150, n_features=1, noise=15, random_state=42)
#
# Tasks:
#   a) Split the data into 70% training and 30% testing (random_state=42)
#   b) Train a LinearRegression model on the training data
#   c) Calculate R² scores for both training and testing sets
#   d) Print both scores and compare them
#   e) Make predictions on the test set and calculate the RMSE
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Binary classification
#
# You have customer data and whether they purchased a product:
#   X represents [age, income] (generate 200 samples with make_classification)
#   y represents purchase (0=no, 1=yes)
#
# Use: X, y = make_classification(n_samples=200, n_features=2, n_informative=2,
#                                 n_redundant=0, random_state=42)
#
# Tasks:
#   a) Split into 80% train, 20% test (random_state=42)
#   b) Train a LogisticRegression model
#   c) Predict on the test set
#   d) Calculate and print the accuracy
#   e) Print the confusion matrix
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Feature scaling
#
# Create data with very different scales:
#   X = np.column_stack([
#       np.random.uniform(100000, 500000, 100),  # Salary
#       np.random.uniform(20, 65, 100)           # Age
#   ])
#   y = (X[:, 0] / 10000 + X[:, 1] * 50 + np.random.normal(0, 100, 100))
#
# Tasks:
#   a) Split into train/test (80/20, random_state=42)
#   b) Create a StandardScaler and fit it on the training data
#   c) Transform both training and test data
#   d) Train a LinearRegression model on the scaled data
#   e) Calculate R² score on scaled test data
#   f) Print the R² score
#
# =============================================================================

def exercise_4():
    np.random.seed(42)
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Decision tree vs logistic regression
#
# Create a classification dataset:
#   X, y = make_classification(n_samples=300, n_features=4, n_informative=3,
#                              random_state=42)
#
# Tasks:
#   a) Split into train/test (75/25, random_state=42)
#   b) Train both a LogisticRegression and DecisionTreeClassifier (max_depth=5)
#   c) Calculate accuracy for both models on the test set
#   d) Print which model performed better
#   e) For the decision tree, print the feature importances
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Complete pipeline with cross-validation
#
# Create a classification dataset:
#   X, y = make_classification(n_samples=400, n_features=5, random_state=42)
#
# Tasks:
#   a) Create a Pipeline with StandardScaler and LogisticRegression
#   b) Split into train/test (80/20, random_state=42)
#   c) Fit the pipeline on training data
#   d) Calculate accuracy on test set
#   e) Perform 5-fold cross-validation on the entire dataset
#   f) Print the mean CV score and standard deviation
#   g) Compare the single test accuracy to the CV mean
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    hours = np.array([[1], [2], [3], [4], [5], [6]])
    scores = np.array([50, 55, 65, 70, 80, 90])

    # a) Create model
    model = LinearRegression()

    # b) Fit
    model.fit(hours, scores)

    # c) Print coefficient and intercept
    print(f"Coefficient: {model.coef_[0]:.2f}")
    print(f"Intercept: {model.intercept_:.2f}")

    # d) Predict for 7 hours
    prediction = model.predict([[7]])
    print(f"Predicted score for 7 hours: {prediction[0]:.1f}")

    # e) R² score
    r2 = model.score(hours, scores)
    print(f"R² score: {r2:.3f}")


def solution_2():
    from sklearn.datasets import make_regression

    X, y = make_regression(n_samples=150, n_features=1, noise=15, random_state=42)

    # a) Split 70/30
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # b) Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # c) Calculate R² scores
    train_r2 = model.score(X_train, y_train)
    test_r2 = model.score(X_test, y_test)

    # d) Print and compare
    print(f"Training R²: {train_r2:.3f}")
    print(f"Testing R²:  {test_r2:.3f}")
    print(f"Difference:  {abs(train_r2 - test_r2):.3f}")

    if abs(train_r2 - test_r2) < 0.1:
        print("Good! Scores are similar - no significant overfitting")
    else:
        print("Warning: Large difference might indicate overfitting")

    # e) Calculate RMSE
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE: {rmse:.2f}")


def solution_3():
    X, y = make_classification(n_samples=200, n_features=2, n_informative=2,
                               n_redundant=0, random_state=42)

    # a) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # b) Train
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # c) Predict
    y_pred = model.predict(X_test)

    # d) Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.3f} ({accuracy * 100:.1f}%)")

    # e) Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print(f"\nConfusion Matrix:")
    print(f"              Predicted")
    print(f"              0    1")
    print(f"Actual 0    {cm[0][0]:3d}  {cm[0][1]:3d}")
    print(f"       1    {cm[1][0]:3d}  {cm[1][1]:3d}")

    print(f"\nTrue Negatives:  {cm[0][0]}")
    print(f"False Positives: {cm[0][1]}")
    print(f"False Negatives: {cm[1][0]}")
    print(f"True Positives:  {cm[1][1]}")


def solution_4():
    np.random.seed(42)
    X = np.column_stack([
        np.random.uniform(100000, 500000, 100),  # Salary
        np.random.uniform(20, 65, 100)           # Age
    ])
    y = (X[:, 0] / 10000 + X[:, 1] * 50 + np.random.normal(0, 100, 100))

    # a) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Before scaling (first 3 samples):")
    print(f"  Salary      Age")
    for i in range(3):
        print(f"  {X_train[i][0]:>9.0f}  {X_train[i][1]:>6.2f}")

    # b) Create and fit scaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    # c) Transform both sets
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print(f"\nAfter scaling (first 3 samples):")
    print(f"  Salary   Age")
    for i in range(3):
        print(f"  {X_train_scaled[i][0]:>7.2f}  {X_train_scaled[i][1]:>6.2f}")

    # d) Train model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # e & f) Calculate and print R² score
    r2 = model.score(X_test_scaled, y_test)
    print(f"\nR² score on scaled data: {r2:.3f}")


def solution_5():
    X, y = make_classification(n_samples=300, n_features=4, n_informative=3,
                               random_state=42)

    # a) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # b) Train both models
    log_model = LogisticRegression(max_iter=1000)
    log_model.fit(X_train, y_train)

    tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)
    tree_model.fit(X_train, y_train)

    # c) Calculate accuracies
    log_accuracy = log_model.score(X_test, y_test)
    tree_accuracy = tree_model.score(X_test, y_test)

    print(f"Logistic Regression accuracy: {log_accuracy:.3f}")
    print(f"Decision Tree accuracy:       {tree_accuracy:.3f}")

    # d) Print better model
    if log_accuracy > tree_accuracy:
        print(f"\nLogistic Regression performed better by {(log_accuracy - tree_accuracy):.3f}")
    elif tree_accuracy > log_accuracy:
        print(f"\nDecision Tree performed better by {(tree_accuracy - log_accuracy):.3f}")
    else:
        print(f"\nBoth models performed equally!")

    # e) Feature importances
    print(f"\nDecision Tree feature importances:")
    for i, importance in enumerate(tree_model.feature_importances_):
        bar = "█" * int(importance * 40)
        print(f"  Feature {i}: {importance:.3f} {bar}")


def solution_6():
    X, y = make_classification(n_samples=400, n_features=5, random_state=42)

    # a) Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=1000))
    ])

    # b) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # c) Fit pipeline
    pipeline.fit(X_train, y_train)

    # d) Test accuracy
    test_accuracy = pipeline.score(X_test, y_test)
    print(f"Test set accuracy: {test_accuracy:.3f}")

    # e) 5-fold cross-validation
    cv_scores = cross_val_score(pipeline, X, y, cv=5)

    # f) Print CV results
    print(f"\n5-fold cross-validation scores:")
    for i, score in enumerate(cv_scores, 1):
        print(f"  Fold {i}: {score:.3f}")

    mean_cv = cv_scores.mean()
    std_cv = cv_scores.std()
    print(f"\nMean CV accuracy: {mean_cv:.3f} (+/- {std_cv * 2:.3f})")

    # g) Compare
    print(f"\nComparison:")
    print(f"  Single test accuracy: {test_accuracy:.3f}")
    print(f"  Mean CV accuracy:     {mean_cv:.3f}")
    print(f"  Difference:           {abs(test_accuracy - mean_cv):.3f}")
    print("\nCV gives a more reliable estimate of model performance!")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Train your first model", exercise_1),
        ("Train/test split", exercise_2),
        ("Binary classification", exercise_3),
        ("Feature scaling", exercise_4),
        ("Decision tree vs logistic regression", exercise_5),
        ("Complete pipeline with cross-validation", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
