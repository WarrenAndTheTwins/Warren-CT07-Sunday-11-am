# print("Hello from lesson 7")

# students = []

# student1 = ["Jimmy", "12345678", "video games"]
# student2 = ["Sarah", "87654321", "soccer"]
# student3 = ["Ryan", "13572468", "basketball"]

# students.append(student1)
# students.append(student2)
# students.append(student3)

# for student in students:
#     name, phone_number, hobby = student
#     print("Name: " + name)
#     print("Phone Number: " + phone_number)
#     print("Hobby: " + hobby)

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]

# ploopy_list = list1 + list2

# print(ploopy_list)

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# ploopy_list = list1 + list2

# pllopy_list = sorted(ploopy_list)

# print(pllopy_list)

# list = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# first_half = list[:3]
# second_half = list[3:]

# print(first_half)
# print(second_half)

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# common = []

# for fruit in list1:
#     if fruit in list2:
#         common.append(fruit)

# print("Common Fruits : ", common)

list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

common = []

for fruit in list1:
    if fruit not in list2:
        common.append(fruit)

print("Common Fruits : ", common)