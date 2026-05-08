# Day 9 - OOP in Python


# Creating a class
class Student:

    # Constructor
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    # Method
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)


# Creating objects
student1 = Student("Prateek", 20, "BTech")
student2 = Student("Rahul", 21, "CSE")


# Calling methods
student1.display_info()

print("----------------")

student2.display_info()