import random

#setting his health and wave number
print("Jimmy Bartholemew the 2nd Jr Sr has 100 health. He must fight through waves of monsters!")
health = 100
counter = 0


while health > 0:
    health_drop = random.randint(1,15)
    print("OOF! Jimmy Bartholemew the 2nd Jr Sr lost " + str(health_drop) + " fighting a monster!")
    counter += 1
    health = health - health_drop

print("Aww, Jimmy Bartholemew the 2nd Jr Sr is drained of health! He survived " + str(counter) + " rounds.")

###########################################################################################################################################################

while True:
    order = input("what would you like to order?")
    list = [""]
    list.append(order)
    if order == "end":
        for orderlol in order:
            food = order
            counter = 0
            counter += 1
            print(str(counter) + ". " + orderlol)