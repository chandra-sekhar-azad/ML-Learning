import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Student_Performance_latest.csv")

# Convert final_grade → Pass/Fail
df["result"] = df["final_grade"].str.lower().apply(
    lambda x: 1 if x in ["a", "b", "c", "d"] else 0
)

# ---- Plot 1: Study Hours vs Result ----
plt.figure()
plt.scatter(df["study_hours"], df["result"])
plt.xlabel("Study Hours")
plt.ylabel("Pass (1) / Fail (0)")
plt.title("Study Hours vs Result")
plt.show()

# ---- Plot 2: Overall Score vs Result ----
plt.figure()
plt.scatter(df["overall_score"], df["result"])
plt.xlabel("Overall Score")
plt.ylabel("Pass (1) / Fail (0)")
plt.title("Overall Score vs Result")
plt.show()

# ---- Plot 3: Age vs Result ----
plt.figure()
plt.scatter(df["age"], df["result"])
plt.xlabel("Age")
plt.ylabel("Pass (1) / Fail (0)")
plt.title("Age vs Result")
plt.show()
