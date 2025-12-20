📘 Day 2 – Data Types & Type Casting
📌 Topics Covered

Built-in Data Types

type() function

Type Casting

📦 Built-in Data Types
Integer (int)
a = 10

Float (float)
b = 10.5

String (str)
name = "Python"

Boolean (bool)
is_valid = True

📂 Collection Data Types
List (mutable)
numbers = [1, 2, 3]

Tuple (immutable)
data = (1, 2, 3)

Set (unique values)
s = {1, 2, 3}

Dictionary (key-value)
student = {"name": "Prateek", "age": 20}

🔍 Checking Data Type
x = 10
print(type(x))

🔄 Type Casting

Converting one data type into another.

String → Integer
a = "10"
b = int(a)

Integer → Float
x = float(5)

Number → String
y = str(100)


⚠ Invalid conversion causes error

int("10.5")  # ❌ Error

🧪 Example Program
a = input("Enter first number: ")
b = input("Enter second number: ")

sum = int(a) + int(b)
print("Sum:", sum)

🎯 Key Points

input() → string

Use type casting for calculations

type() helps in debugging

🎥 YouTube Resource (Code With Harry)

👉 Code With Harry – Python Tutorial (Data Types)
(Search: “Code With Harry Python Data Types”)

📝 Practice

Convert string to int

Add two numbers

Create a list and print it

Print type of each variable