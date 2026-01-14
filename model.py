import pandas as pd
import numpy as np

data=pd.read_csv("Student_Performance_latest.csv")

# print(data.head())
min_age = data['age'].min()
max_age = data['age'].max()

# print("Minimum Age:", min_age)
# print("Maximum Age:", max_age)
# print(data.info())

# print(data['extra_activities'].unique())
# print(data['parent_education'].unique())
# print(data['school_type'].unique())

#her i changed all other educations into either educated or not educated
mapping = {
    'no formal': 'not educated',
    'not educated': 'not educated',   # keep safe if rerun
    'graduate': 'educated',
    'post graduate': 'educated',
    'high school': 'educated',
    'diploma': 'educated',
    'phd': 'educated',
    'educated': 'educated'            # keep safe if rerun
}

data['parent_education'] = data['parent_education'].map(mapping)
