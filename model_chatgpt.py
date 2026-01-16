import pandas as pd

# -----------------------
# Load dataset
# -----------------------
df = pd.read_csv("Student_Performance_latest.csv")

# -----------------------
# 1. Convert final_grade → Pass / Fail
# a,b,c,d = Pass | e,f = Fail
# -----------------------
df["result"] = df["final_grade"].str.lower().apply(
    lambda x: "Pass" if x in ["a", "b", "c", "d"] else "Fail"
)

# -----------------------
# 2. Simplify parent education
# -----------------------
educated_levels = ["bachelor", "graduate", "post graduate", "master", "phd"]

df["parent_edu_simple"] = df["parent_education"].str.lower().apply(
    lambda x: "Educated" if x in educated_levels else "Uneducated"
)

# -----------------------
# 3. Select required columns
# -----------------------
data = df[[
    "study_hours",
    "overall_score",
    "study_method",
    "extra_activities",
    "parent_edu_simple",
    "result"
]]

# -----------------------
# 4. Encode categorical columns
# (study_method, extra_activities, parent_edu_simple, result)
# -----------------------
data_encoded = pd.get_dummies(data, drop_first=True)

# -----------------------
# 5. Create X (features) and y (target)
# -----------------------
X = data_encoded.drop("result_Pass", axis=1).values
y = data_encoded["result_Pass"].values

# -----------------------
# Output shapes (verification)
# -----------------------
print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nFirst 2 rows of X:")
print(X[:2])

print("\nFirst 10 values of y:")
print(y[:10])
