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


