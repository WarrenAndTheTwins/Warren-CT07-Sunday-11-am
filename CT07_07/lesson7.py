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

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# unique = []

# for fruit in list1:
#     if fruit not in list2:
#         unique.append(fruit)

# print("Unique Fruits : ", unique)

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# list3 = [x for x in list1 + list2 if x % 2 == 0]

# print("Merged list with numbers divisible by a positive integer that is both prime and even:", list3)

# nested_list = [[1, 2], [3, 4], [5, 6]]
# new_list = []

# for minilist in nested_list:
#     for student in minilist:
#         new_list.append(student)

# print("Flattened list:", new_list)

# students = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# potato = students[:3]
# print(potato)
# potati = students[3:6]
# print(potati)
# potata = students[6:9]
# print(potata)

import random

spelling_bee = [
    ["besieged", "/bɪˈsiːdʒd/"],
    ["caffeine", "/ˈkæf.iːn/"],
    ["cameist", "/ˈkeɪ.mɪst/"],
    ["deceitful", "/dɪˈsiːt.fəl/"],
    ["holstein", "/ˈhoʊl.staɪn/"],
    ["neighbor", "/ˈneɪbər/"],
    ["seize",  "/siːz/"],
    ["weird", "/wɪrd/"],
    ["leisure", "/ˈliːʒər/"],
    ["conceit", "/kənˈsiːt/"],
    ["perceive", "/pərˈsiːv/"],
    ["Rein", "/reɪn/"],
    ["feign", "/feɪn/"],
    ["reveille", "/ˈrɛvəli/"],
    ["Seismic", "/ˈsaɪzmɪk/"],
    ["Rietveld", "/ˈritfɛld/"],
    ["Deictic", "/ˈdaɪktɪk/"],
    ["Einsteinian", "/ˌaɪnˈstaɪniən/"],
    ["Eiderdown", "/ˈaɪdərdaʊn/"],
    ["Rietveld", "/ˈritfɛld/"],
    ["Zeitgeber", "/ˈtsaɪtˌɡeɪbər/"],
    ["Beige", "/beɪʒ/"],
    ["Riesling", "/ˈriːslɪŋ/"],
    ["Eidetic", "/aɪˈdɛtɪk/"]
    ["Surveil", "/sərˈveɪl/"]
    ["Feint", "/feɪnt/"]
]

while True:

    random_word = random.choice(spelling_bee)
    wordlol, pronunciation = random_word

    print(pronunciation)

    spelling = input("Spell!")

    if spelling == wordlol:
        print("Yay!")
    else:
        print("Nope.")