# Writing to file
file = open("sample.txt", "w")

file.write("Hello Prateek\n")
file.write("Welcome to Python")

file.close()

# Reading file
file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()

# Exception handling
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program ended")
    