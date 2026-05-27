import pandas as pd

df = pd.read_csv("students.csv")

print("Complete data")
print(df)

print("\nNames only")
print(df["Name"])

print("\nName and Marks")
print(df[["Name","Marks"]])

print("\nMarks > 80")
print(df[df["Marks"] > 80])

print("\nSorted by Marks")
print(df.sort_values("Marks", ascending=False))