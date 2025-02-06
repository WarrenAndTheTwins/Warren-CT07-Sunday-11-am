# print("Hello from lesson 3")
# timer = 1
# import time

# int(timer) == input("how long is ur study time?")
# while timer > 0:
#     print (timer)
#     time.sleep(60)
#     timer -= 1
# print("U dumdum, so keep studying.")

# savings = 0

# savings_today = input("How much you save today?")
# savings = savings + float(savings_today)
# while savings < 100:
#     print("You have " + str(savings) + " dollars. You have to save " + str(100 - float(savings)) + " mor monies. You currently have not reached ur goal. You are not cool.")
#     savings_today = input("How much you save today?")
#     savings = savings + float(savings_today)
# print("U suck. Noone likes u. Your free trial has ended, now you must pay " + str(savings) + " dollars.")

import random

life = 1.4
quotient1 = random.randint(2,20)
quotient2 = random.randint(2,20)
questions = 0
product = 90876
print("LOL HERE IS QUIZ no way u smart enough to win")
while life > 0:
    product_lol = input("What is " + str(quotient1) + " x " + str(quotient2) + "?")
    product = quotient1 * quotient2
    if int(product_lol) != product:
        product_lol = input("What is " + str(quotient1) + " x " + str(quotient2) + "?")
        life -= 1
    else:
        quotient1 = random.randint(2,20)
        quotient2 = random.randint(2,20)
        questions += 1
        life = 3
if questions < 15:
    "YOU NEED TO LEAVE!"
else:
    "u pretty good!"

