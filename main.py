import pandas as pd
import numpy as np
from functions import *

# Step 1 - read the data
df = pd.read_csv("students.csv")
print("Number of records:", len(df))
print("Columns:", list(df.columns))
print(df.head())

# Step 2 - process the data
df = calculate_total(df)
df = calculate_average(df)
df = add_grades(df)
df = add_result(df)

print("\n--- Student Report ---")
print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]])

# Step 3 - highest, lowest and class average
top = df.loc[df["Average"].idxmax()]
low = df.loc[df["Average"].idxmin()]
print("\nHighest average:", top["Name"], "-", top["Average"])
print("Lowest average:", low["Name"], "-", low["Average"])
print("Class average:", round(np.mean(df["Average"]), 2))

# Step 4 - pass / fail
passed = len(df[df["Result"] == "Pass"])
failed = len(df[df["Result"] == "Fail"])
print("\nStudents passed:", passed)
print("Students failed:", failed)

# Step 5 - subject wise analysis
print("\n--- Subject-wise Average ---")
best_subject = ""
best_avg = 0
for sub in subjects:
    avg = np.mean(df[sub])
    print(sub, ":", round(avg, 2))
    if avg > best_avg:
        best_avg = avg
        best_subject = sub
print("Best subject:", best_subject)

# Step 6 - top 5 students
print("\n--- Top 5 Students ---")
top5 = df.sort_values("Average", ascending=False).head(5)
print(top5[["Name", "Total", "Average", "Grade"]])