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

# sales_data =[
#     ["Apple", 50, 1.99],
#     ["Banana", 45, 0.99],
#     ["Orange", 30, 2.49],
#     ["Grapefruit", 25, 3.99],
#     ["Mango", 20, 2.99]
# ]
# earned = []
# for fruit, units, cost in sales_data:
#     earned.append (units * cost)

# top_fruits = []
# max_value = 0
# for price in earned:
#     if max_value < price:
#         max_value = price
        
# print(max_value)

# for fruit in sales_data:
#     fruit_max = fruit[earned.index(max_value)]
# print(fruit_max)

# isCorrect = False
# eggprobs = input("What has to be broken before you use it?")
# eggprobs = eggprobs.lower()
# list = eggprobs.split(" ")
# for i in list:
#     if i == "egg":
#         isCorrect = True
# if isCorrect == True:
#     print("Nice! You're pretty smart!")
# else:
#     print("BIG DUMBHEADDDDD")

import turtle

window = turtle.Screen()
window.setup(600,600)
window.bgcolor("forestgreen")
pen = turtle.Turtle()
pen.penup()
pen.shape("square")
pen.sety(250)
for i in range(-300,300,25):
    pen.setx(i)
    pen.stamp()
pen.goto(-300, -250)
pen.pencolor("yellow")
pen.pendown()
pen.seth(0)
pen.forward(600)
pen.hideturtle()

Plippy = turtle.Turtle()
Plippy.penup

window.mainloop()

