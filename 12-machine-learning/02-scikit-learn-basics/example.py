"""
scikit-learn Basics — Example Code
===================================

Run this file:
    python3 example.py

A hands-on tour of scikit-learn fundamentals. Each section demonstrates a core
concept with real output so you can see exactly what's happening.
"""

import sys

try:
    import numpy as np
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
    from sklearn.metrics import confusion_matrix, classification_report
    from sklearn.pipeline import Pipeline
    from sklearn.datasets import make_regression, make_classification
except ImportError:
    print("This lesson requires scikit-learn and numpy.")
    print("Install them with: pip install scikit-learn numpy")
    print("Then try again!")
    sys.exit(0)


# =============================================================================
# 1. The scikit-learn pattern — fit, predict, score
# =============================================================================

print("=" * 70)
print("1. THE SCIKIT-LEARN PATTERN")
print("=" * 70)

# Create simple synthetic data
np.random.seed(42)
X_simple = np.array([[1], [2], [3], [4], [5]])
y_simple = np.array([2, 4, 6, 8, 10])  # y = 2 * X

print("Data:")
for i in range(len(X_simple)):
    print(f"  X={X_simple[i][0]}, y={y_simple[i]}")

# The three-step pattern
model = LinearRegression()              # 1. Create
model.fit(X_simple, y_simple)           # 2. Fit (train)
predictions = model.predict(X_simple)   # 3. Predict

print(f"\nPredictions: {predictions}")
print(f"Model coefficient: {model.coef_[0]:.2f}")
print(f"Model intercept: {model.intercept_:.2f}")
print(f"R² score: {model.score(X_simple, y_simple):.3f}")
print()


# =============================================================================
# 2. Train/test split — evaluating on unseen data
# =============================================================================

print("=" * 70)
print("2. TRAIN/TEST SPLIT")
print("=" * 70)

# Generate more realistic data
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

print(f"Total samples: {len(X)}")

# Split into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Train on training data only
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate on both sets
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"\nR² on training data: {train_score:.3f}")
print(f"R² on testing data:  {test_score:.3f}")
print("(Scores should be similar — if test is much lower, we're overfitting)")
print()


# =============================================================================
# 3. Linear regression — predicting house prices
# =============================================================================

print("=" * 70)
print("3. LINEAR REGRESSION — HOUSE PRICES")
print("=" * 70)

# Simulate house data: size (sqft), bedrooms, age
np.random.seed(42)
n_houses = 200

# Features: [size, bedrooms, age]
sizes = np.random.uniform(800, 3000, n_houses)
bedrooms = np.random.randint(1, 6, n_houses)
ages = np.random.uniform(0, 50, n_houses)

# Price formula with some noise
prices = (sizes * 150 + bedrooms * 20000 - ages * 1000 +
          np.random.normal(0, 20000, n_houses))

X = np.column_stack([sizes, bedrooms, ages])
y = prices

print(f"Dataset: {n_houses} houses with 3 features")
print(f"Features: [size (sqft), bedrooms, age (years)]")
print(f"\nFirst 3 houses:")
print(f"  Size  Beds  Age   Price")
for i in range(3):
    print(f"  {sizes[i]:5.0f}  {bedrooms[i]:2d}   {ages[i]:4.1f}  ${prices[i]:>8.0f}")

# Split and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"\nModel performance:")
print(f"  R² score: {r2:.3f}")
print(f"  RMSE: ${rmse:,.0f}")

print(f"\nFeature coefficients:")
features = ["Size (sqft)", "Bedrooms", "Age (years)"]
for feature, coef in zip(features, model.coef_):
    print(f"  {feature:15s}: ${coef:>8.2f}")

print(f"\nSample predictions vs actual:")
for i in range(3):
    print(f"  Predicted: ${y_pred[i]:>8.0f}  |  Actual: ${y_test[i]:>8.0f}")
print()


# =============================================================================
# 4. Classification — spam detection
# =============================================================================

print("=" * 70)
print("4. LOGISTIC REGRESSION — SPAM DETECTION")
print("=" * 70)

# Generate synthetic email data
# Features: word count, special chars, has_links, caps_ratio
np.random.seed(42)
n_emails = 500

# Spam emails have more special chars, links, and caps
spam_features = np.column_stack([
    np.random.uniform(50, 200, n_emails // 2),    # word_count
    np.random.uniform(15, 40, n_emails // 2),     # special_chars
    np.random.uniform(0.7, 1.0, n_emails // 2),   # has_links (probability)
    np.random.uniform(0.3, 0.8, n_emails // 2)    # caps_ratio
])

# Regular emails have fewer special chars, links, and caps
regular_features = np.column_stack([
    np.random.uniform(20, 150, n_emails // 2),
    np.random.uniform(2, 15, n_emails // 2),
    np.random.uniform(0.0, 0.3, n_emails // 2),
    np.random.uniform(0.0, 0.2, n_emails // 2)
])

X = np.vstack([spam_features, regular_features])
y = np.array([1] * (n_emails // 2) + [0] * (n_emails // 2))  # 1=spam, 0=regular

print(f"Dataset: {n_emails} emails")
print(f"Features: [word_count, special_chars, has_links, caps_ratio]")
print(f"Spam emails: {np.sum(y == 1)}")
print(f"Regular emails: {np.sum(y == 0)}")

# Split and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.3f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(f"\nConfusion Matrix:")
print(f"                 Predicted")
print(f"                 Regular  Spam")
print(f"Actual Regular     {cm[0][0]:3d}    {cm[0][1]:3d}")
print(f"       Spam        {cm[1][0]:3d}    {cm[1][1]:3d}")

print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Regular', 'Spam']))
print()


# =============================================================================
# 5. Decision tree classifier — email classification
# =============================================================================

print("=" * 70)
print("5. DECISION TREE CLASSIFIER")
print("=" * 70)

# Use the same email data from above
tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)
tree_model.fit(X_train, y_train)

y_pred_tree = tree_model.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_pred_tree)

print(f"Decision Tree accuracy: {accuracy_tree:.3f}")
print(f"Logistic Regression accuracy: {accuracy:.3f}")

# Feature importance
print(f"\nFeature importance (how much each feature matters):")
features = ["word_count", "special_chars", "has_links", "caps_ratio"]
for feature, importance in zip(features, tree_model.feature_importances_):
    bar = "█" * int(importance * 50)
    print(f"  {feature:15s} {importance:.3f} {bar}")
print()


# =============================================================================
# 6. Feature scaling — why it matters
# =============================================================================

print("=" * 70)
print("6. FEATURE SCALING")
print("=" * 70)

# Generate data with different scales
np.random.seed(42)
X_unscaled = np.column_stack([
    np.random.uniform(1000, 5000, 100),    # Large values (salary)
    np.random.uniform(1, 10, 100)           # Small values (years experience)
])
y = (X_unscaled[:, 0] * 0.1 + X_unscaled[:, 1] * 1000 +
     np.random.normal(0, 500, 100))

X_train, X_test, y_train, y_test = train_test_split(
    X_unscaled, y, test_size=0.2, random_state=42
)

print("Original data (first 3 samples):")
print("  Salary  Experience")
for i in range(3):
    print(f"  {X_train[i][0]:6.0f}    {X_train[i][1]:5.2f}")

# Train without scaling
model_unscaled = LinearRegression()
model_unscaled.fit(X_train, y_train)
score_unscaled = model_unscaled.score(X_test, y_test)

# Train with scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Important: use same scaler!

print(f"\nScaled data (first 3 samples):")
print("  Salary  Experience")
for i in range(3):
    print(f"  {X_train_scaled[i][0]:6.2f}    {X_train_scaled[i][1]:6.2f}")

model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)
score_scaled = model_scaled.score(X_test_scaled, y_test)

print(f"\nR² without scaling: {score_unscaled:.3f}")
print(f"R² with scaling:    {score_scaled:.3f}")
print("(For linear regression, scaling doesn't change R², but it helps with")
print(" interpretation and is crucial for many other algorithms like SVM)")
print()


# =============================================================================
# 7. Cross-validation — more reliable evaluation
# =============================================================================

print("=" * 70)
print("7. CROSS-VALIDATION")
print("=" * 70)

# Generate classification data
X, y = make_classification(n_samples=200, n_features=5, n_informative=3,
                           n_redundant=1, random_state=42)

print("Instead of a single train/test split, we test multiple times.")
print("This gives a more reliable estimate of model performance.")

# Single train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
single_score = model.score(X_test, y_test)

print(f"\nSingle train/test split accuracy: {single_score:.3f}")

# 5-fold cross-validation
model = LogisticRegression(max_iter=1000)
cv_scores = cross_val_score(model, X, y, cv=5)

print(f"\n5-fold cross-validation scores:")
for i, score in enumerate(cv_scores, 1):
    print(f"  Fold {i}: {score:.3f}")

print(f"\nMean accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
print("This is a more trustworthy estimate than a single split!")
print()


# =============================================================================
# 8. Pipelines — combining preprocessing and modeling
# =============================================================================

print("=" * 70)
print("8. PIPELINES — CLEANER WORKFLOWS")
print("=" * 70)

# Generate data
X, y = make_classification(n_samples=300, n_features=4, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Without pipeline (manual steps):")
print("  1. Create scaler")
print("  2. Fit scaler on training data")
print("  3. Transform training data")
print("  4. Transform test data")
print("  5. Train model")
print("  6. Make predictions")

# Manual approach
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
score_manual = model.score(X_test_scaled, y_test)

print(f"\nManual accuracy: {score_manual:.3f}")

print("\nWith pipeline (automatic):")
print("  1. Define pipeline")
print("  2. Fit pipeline")
print("  3. Predict")

# Pipeline approach
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
score_pipeline = pipeline.score(X_test, y_test)

print(f"\nPipeline accuracy: {score_pipeline:.3f}")
print("\nBenefits:")
print("  - Cleaner code")
print("  - No risk of forgetting to scale test data")
print("  - Easy to add more preprocessing steps")
print("  - Simple to deploy")
print()


# =============================================================================
# 9. Complete example — predicting student performance
# =============================================================================

print("=" * 70)
print("9. COMPLETE EXAMPLE — STUDENT PERFORMANCE")
print("=" * 70)

# Simulate student data
np.random.seed(42)
n_students = 300

# Features
study_hours = np.random.uniform(1, 10, n_students)
attendance = np.random.uniform(0.4, 1.0, n_students)
prev_score = np.random.uniform(40, 95, n_students)
sleep_hours = np.random.uniform(4, 9, n_students)

# Final score based on features with some noise
final_score = (study_hours * 5 +
               attendance * 30 +
               prev_score * 0.3 +
               sleep_hours * 2 +
               np.random.normal(0, 5, n_students))

# Clip to realistic range
final_score = np.clip(final_score, 0, 100)

X = np.column_stack([study_hours, attendance, prev_score, sleep_hours])
y = final_score

print(f"Dataset: {n_students} students")
print(f"Features: [study_hours, attendance, prev_score, sleep_hours]")
print(f"Target: final_score (0-100)")

print(f"\nFirst 5 students:")
print("  Study  Attend  PrevScore  Sleep  Final")
for i in range(5):
    print(f"   {study_hours[i]:4.1f}   {attendance[i]:5.2f}     {prev_score[i]:5.1f}   {sleep_hours[i]:4.1f}  {final_score[i]:5.1f}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\nModel performance:")
print(f"  R² score: {r2:.3f}")
print(f"  RMSE: {rmse:.2f} points")

# Get coefficients (need to access the model inside the pipeline)
coefficients = pipeline.named_steps['regressor'].coef_
features = ["Study Hours", "Attendance", "Prev Score", "Sleep Hours"]

print(f"\nFeature importance (coefficients):")
for feature, coef in zip(features, coefficients):
    print(f"  {feature:12s}: {coef:>6.2f}")

# Cross-validation
cv_scores = cross_val_score(pipeline, X, y, cv=5,
                           scoring='r2')

print(f"\n5-fold cross-validation:")
print(f"  Mean R²: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

# Make predictions for new students
print(f"\nPredicting for new students:")
new_students = np.array([
    [8.0, 0.95, 85, 7],   # Good student
    [2.0, 0.50, 60, 5],   # Struggling student
    [6.0, 0.80, 75, 6.5]  # Average student
])

new_predictions = pipeline.predict(new_students)

student_types = ["Good student", "Struggling student", "Average student"]
for i, (student_type, pred) in enumerate(zip(student_types, new_predictions)):
    print(f"  {student_type}:")
    print(f"    Study={new_students[i][0]:.1f}h, Attendance={new_students[i][1]:.0%}, "
          f"PrevScore={new_students[i][2]:.0f}, Sleep={new_students[i][3]:.1f}h")
    print(f"    Predicted final score: {pred:.1f}")

print()


# =============================================================================
# Final summary
# =============================================================================

print("=" * 70)
print("   SCIKIT-LEARN BASICS COMPLETE!")
print("=" * 70)
print()
print("Key takeaways:")
print("  1. fit() trains the model, predict() makes predictions")
print("  2. Always split your data (train/test) to evaluate properly")
print("  3. Scale your features for many algorithms")
print("  4. Use cross-validation for more reliable evaluation")
print("  5. Pipelines make your code cleaner and safer")
print()
print("Try the exercises in exercises.py to test your understanding!")
