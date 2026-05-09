# Day 11 - NumPy Basics

import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])

print("Array:")
print(arr1)

# Array operations
print("\nAdd 2:")
print(arr1 + 2)

print("\nMultiply by 3:")
print(arr1 * 3)

# Array properties
print("\nShape:")
print(arr1.shape)

print("\nData type:")
print(arr1.dtype)

# 2D Array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr2)

# Accessing elements
print("\nFirst element:", arr1[0])
print("Element at row 1 col 2:", arr2[0][1])