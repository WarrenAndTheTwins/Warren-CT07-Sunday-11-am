print("Hello from lesson 7")

students = []

student1 = ["Jimmy", "12345678", "video games"]
student2 = ["Sarah", "87654321", "soccer"]
student3 = ["Ryan", "13572468", "basketball"]

students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    name, phone_number, hobby = student