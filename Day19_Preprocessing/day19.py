import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Dataset
data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 50000, 70000, 100000]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# Feature Scaling

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

print("\nScaled Data")
print(scaled_data)

# Train Test Split

X_train, X_test = train_test_split(
    scaled_data,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data")
print(X_train)

print("\nTesting Data")
print(X_test)