import pandas as pd

# Read CSV
df = pd.read_csv("dirty_data.csv")

print("Original Data")
print(df)

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing marks with 0
df["Marks"] = df["Marks"].fillna(0)

print("\nAfter Filling Missing Values")
print(df)

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter Removing Duplicates")
print(df)