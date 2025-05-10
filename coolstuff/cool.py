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
    if difficulty in ["e", "E", "ez", "easy"]:
        if guessgame(1, 5): 
            print("Correct")
        else:
            print("Incorrect")
    elif difficulty in ["m", "M", "medium"]:
        if guessgame(1, 10): 
            print("Correct")
        else:
            print("Incorrect")
    elif difficulty in ["H" or "h" or "hard"]:
        if guessgame(1, 25): 
            print("Correct")
        else:
            print("Incorrect")
    elif difficulty == "I" or "i" or "impossible":
        if guessgame(1, 100): 
            print("Correct")
        else:
            print("Incorrect")
    else: 
        print("Sorry, choose something else.")