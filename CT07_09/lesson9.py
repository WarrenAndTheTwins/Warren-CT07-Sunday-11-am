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
import random

guess = input("Guess the winner!")

winner = ""
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
Plippy.penup()
Plippy.seth(90)
Plippy.shape("turtle")
Plippy.color("#9A3836")
Plippy.goto(0,-250)
Plippy.write("Plippy", align = "center", font =('Futura', 20))

Glob = turtle.Turtle()
Glob.penup()
Glob.seth(90)
Glob.shape("turtle")
Glob.color("white")
Glob.goto(-200,-250)
Glob.write("Glob", align = "center", font =('Futura', 20))

Bippy = turtle.Turtle()
Bippy.penup()
Bippy.seth(90)
Bippy.shape("turtle")
Bippy.color("green")
Bippy.goto(200,-250)
Bippy.write("Bippy", align = "center", font =('Futura', 20))

Plippy.pendown()
Glob.pendown()
Bippy.pendown()

while True:
    Plippy.seth(random.randint(75, 120))
    Glob.seth(random.randint(75, 120))
    Bippy.seth(random.randint(75, 120))

    Plippy.forward(random.randint(1, 20))
    Glob.forward(random.randint(1, 20))
    Bippy.forward(random.randint(1, 20))

    if Plippy.ycor() >250:
        winner = "Plippy"
        break
    if Glob.ycor() >250:
        winner = "Plippy"
        break
    if Bippy.ycor() >250:
        winner = "Plippy"
        break
if guess == winner:
    print("nice u got it right")
else:
    print("Nah bro it was " + winner + " better luck next time")

window.mainloop()



