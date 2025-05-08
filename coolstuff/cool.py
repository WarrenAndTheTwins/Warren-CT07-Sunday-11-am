import random

ans = 1
def guessgame(min, max):
    ans = random.randint(min, max)
    guess = input("Guess a number between "+ str(min) + " and " + str(max) + ".")
    if guess == ans:
        return True
    else:
        return False

while True:
    if guessgame(1, 10): 
        print("yay")
    else:
        print("awww")

