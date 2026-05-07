# Dictionary example

student = {
    "name": "Prateek",
    "age": 20,
    "branch": "BTech"
}

print(student)

# Access values
print(student["name"])
print(student.get("age"))

# Update value
student["age"] = 21

# Add new key
student["college"] = "VIT"

print(student)

# String operations

text = "python programming"

print(text.upper())
print(text.lower())
print(len(text))
print(text[0:6])

new_text = text.replace("python", "java")
print(new_text)