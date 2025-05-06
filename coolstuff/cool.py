import random

ans = 0
def guessgame(min, max):
    ans = random.randint(min, max)
    input("Guess a number between " + min + " and " + max + ".")

