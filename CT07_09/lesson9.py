# while True:
#     word = input("Word?")
#     if word == word[::-1]:
#         print("YAYAYYA")
#     else:
#         print("nope")

# sentence = input("sentence pls")
# palindromes = 0
# list = sentence.split(" ")
# palindromelist = [""]
# for word in list:
#     if word == word[::-1]:
#         palindromelist.append(word)
#         palindromes += 1

# print(palindromes)
# print(palindromelist)

sales_data =[
    ["Apple", 50, 1.99],
    ["Banana", 45, 0.99],
    ["Orange", 30, 2.49],
    ["Grapefruit", 25, 3.99],
    ["Mango", 20, 2.99]
]
for fruit, units, cost in sales_data:
    total_monies = units * cost

print("Top 3 sellers")
    