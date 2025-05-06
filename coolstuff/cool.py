import random

ans = 0
def guessgame(min, max):
    ans = random.randint(min, max)
    guess = input(f"Guess a number between " + {min} + " and " + max + ".")
    if ans == guess:
        return True
    else:
        return False
guessgame(1, 10)

