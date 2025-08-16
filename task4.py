# Task 4 - Iris Dataset Classification with Model Save/Load

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import joblib

# ---------------------------
# Step 1: Load Dataset
# ---------------------------
iris = load_iris()
X = iris.data
y = iris.target

# ---------------------------
# Step 2: Train-Test Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ---------------------------
# Step 3: Train Model
# ---------------------------
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# ---------------------------
# Step 4: Predictions
# ---------------------------
y_pred = model.predict(X_test)

# ---------------------------
# Step 5: Confusion Matrix
# ---------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d",
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Iris Classification")
plt.show()

# ---------------------------
# Step 6: Classification Report
# ---------------------------
print("\nClassification Report - Iris Classification\n")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ---------------------------
# Step 7: Save the Model
# ---------------------------
joblib.dump(model, "iris_model.pkl")
print("\n✅ Model saved as iris_model.pkl")

# ---------------------------
# Step 8: Load & Test Model
# ---------------------------
loaded_model = joblib.load("iris_model.pkl")
print("✅ Loaded model accuracy:", loaded_model.score(X_test, y_test))
