print("Hello from lesson 10")
import turtle
# def alert():
#     print("MOTION DETECTED")
# t = turtle.Turtle()

# def square():
#     for i in range (4):
#         t.forward(20)
#         t.left(90)

# def domath(num1, num2, num3):
#     print(str(num1 * num3 / num2 + num1 - num2 * num3))

# domath(1,999,0)
    

# calculate squares
# num = 3

# square1 = num * num
# square2 = num**2 # to the power of 2

# import math
# square3 = math.pow(num,2)

# print(square1)
# print(square2)
# print(square3)



# define a function to calculate the square of a number
# return the square


# 35, 67, 972 (calculate the squares of these 3 numbers using the function)

# calculate the total sum of these 3 (squares???)

# def exponent(num,exponent):
#     ans = num**exponent 
#     return ans

# sum = 0 

# for i in range(3):
#     originalnum = int(input("num plz?"))
#     originalexponent = int(input("exponent plz?"))
#     square = exponent(originalnum, originalexponent)
#     sum += square
# print(f"The sum of the three things is: {sum}" )

import random

def diceGuess(guess):
    randompotato = random.randint(1,6)
    if randompotato == guess:
        return True
    else:
        return False
    


while True:
    gaaaaauiiooo = int(input("guessssss: "))

    if diceGuess(gaaaaauiiooo):
        print("Your guess is correct")
        break
    else:
        print("Your guess is wrong.")


    