import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("Student_Performance_latest.csv")

# -----------------------------------
# 1. Convert final_grade → Pass / Fail
# -----------------------------------
df["result"] = df["final_grade"].apply(
    lambda x: "Pass" if x in ["a", "b", "c", "d"] else "Fail"
)

# -----------------------------------
# 2. Simplify parent_education
# -----------------------------------
df["parent_education_simple"] = df["parent_education"].apply(
    lambda x: "Educated" if x in ["graduate", "post graduate"] else "Not Educated"
)

# -----------------------------------
# 3. Select only required input features
# -----------------------------------
X = df[
    [
        "school_type",
        "parent_education_simple",
        "study_hours",
        "attendance_percentage",
        "extra_activities",
        "study_method",
        "overall_score"
    ]
]

y = df["result"]

# -----------------------------------
# 4. One-Hot Encode categorical inputs
# -----------------------------------
X_encoded = pd.get_dummies(X)

# -----------------------------------
# 5. Encode output (Pass/Fail)
# -----------------------------------
le = LabelEncoder()
y_encoded = le.fit_transform(y)   # Fail = 0, Pass = 1

# -----------------------------------
# 6. Train-test split
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y_encoded, test_size=0.2, random_state=42
)

# -----------------------------------
# 7. Train model
# -----------------------------------
model = DecisionTreeClassifier(max_depth=6, random_state=42)
model.fit(X_train, y_train)

# -----------------------------------
# 8. Evaluate
# -----------------------------------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

from sklearn.metrics import precision_score, recall_score, f1_score

print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
