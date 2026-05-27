import matplotlib.pyplot as plt

# Data 
months = ["jan","Feb","Mar","Apr","May"]
sales = [100,200, 250, 300, 250]

#Line Graph 
plt.plot(months, sales)

import matplotlib.pyplot as plt

students = ["Prateek", "Rahul", "Aman"]
marks = [85, 90, 78]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

subjects = ["Python", "ML", "DSA"]
hours = [5, 3, 2]

plt.pie(hours, labels=subjects, autopct="%1.1f%%")

plt.title("Study Time Distribution")

plt.show()