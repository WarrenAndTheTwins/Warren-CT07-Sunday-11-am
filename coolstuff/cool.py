import random

guess = 0
def guessgame(min, max):
    guess = random.randint(min, max)
    input("Guess a number between " + min + " and " + max + ".")
    
