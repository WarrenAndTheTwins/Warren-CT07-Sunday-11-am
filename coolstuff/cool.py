import random

def guessgame(min, max):
    ans = random.randint(min, max)
    guess = int(input("Guess a number between "+ str(min) + " and " + str(max) + "."))
    if guess == ans:
        return True
    else:
        return False

while True:
    difficulty = input("What difficulty do you choose?") 
    if difficulty == "e" or "E" or "ez" or "easy":
        if guessgame(1, 5): 
            print("Correct")
        else:
            print("Incorrect")
    elif difficulty == "M" or "m" or "medium":
        if guessgame(1, 10): 
            print("yay")
        else:
            print("Incorrect")
    elif difficulty == "H" or "h" or "hard":
        if guessgame(1, 25): 
            print("yay")
        else:
            print("Incorrect")
 
