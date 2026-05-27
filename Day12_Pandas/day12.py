import pandas as pd

# Create DataFrame

data = {
    "Name": ["Prateek","Rahul", "Aman"],
    "Age": [20, 21, 22],
    "Marks": [85,90,78]
}

df = pd.DataFrame(data)

print("DaraFrame:")
print(df)

print("\nShape:")
print(df.shape)
print("\nInformation:")
print(df.info())

print("\nFirst Rows:")
print(df.head())

df2 = pd.read_csv("students.csv")

print("\nCSV Data:")
print(df2)