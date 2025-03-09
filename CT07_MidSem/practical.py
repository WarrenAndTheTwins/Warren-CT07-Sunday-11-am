import random

print("Jimmy Bartholemew the 2nd Jr Sr has 100 health. He must fight through waves of monsters!")
health = 100
counter = 0

while health > 0:
    health_drop = random.randint(1,15)
    print("OOF! Jimmy Bartholemew the 2nd Jr Sr lost " + health_drop + " fighting a monster!")
    counter += 1
print("Aww, Jimmy Bartholemew the 2nd Jr Sr is drained of health! He survived " + " rounds.")