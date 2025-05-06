import random

ans = 0
def guessgame(min, max):
    ans = random.randint(min, max)
    guess = input("Guess a number between "+ str(min) + " and " + str(max) + ".")
    if ans == guess:
        return True
    else:
        return False
guessgame(1, 10)

