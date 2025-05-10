import random

streak = 0
 
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
            streak = 0
    elif difficulty in ["m", "M", "medium"]:
        if guessgame(1, 10): 
            print("Correct")
            streak += 1
        else:
            print("Incorrect")
            streak = 0
    elif difficulty in ["H", "h", "hard"]:
        if guessgame(1, 25): 
            print("Correct")
            streak += 1
        else:
            print("Incorrect")
            streak = 0
    elif difficulty in ["I", "i", "impossible"]:
        if guessgame(1, 100): 
            print("Correct")
            streak += 1
        else:
            print("Incorrect")
            streak = 0
    elif difficulty in ["streak", "Streak"]:
        print("Your streak is at " + streak + ".")
    else: 
        print("Sorry, choose something else.")