import random

def guessgame(min, max):
    ans = random.randint(min, max)
    guess = int(input("Guess a number between "+ str(min) + " and " + str(max) + "."))
    if guess == ans:
        return True
    else:
        return False

while True:
    print("What difficulty do you choose?") 

    if guessgame(1, 10): 
        print("yay")
    else:
        print("awww")

