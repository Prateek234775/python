# Student Management Mini Project


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_result(self):

        if self.marks >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Result: {result}")


# Taking input
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

# Creating object
s1 = Student(name, marks)

# Display result
s1.show_result()