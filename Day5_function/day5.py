# simple function
def greet():
    print("Hello, welcome to Python")

greet()

# function with parameter
def greet_user(name):
    print("Hello", name)

greet_user("Prateek")

# function with return value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)