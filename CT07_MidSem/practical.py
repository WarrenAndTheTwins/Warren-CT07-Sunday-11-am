import random

#setting his health and wave number
print("Jimmy Bartholemew the 2nd Jr Sr has 100 health. He must fight through waves of monsters!")
health = 100
counter = 0

#setting up the loop for his repeated attacks
while health > 0:
    health_drop = random.randint(1,15)
    print("OOF! Jimmy Bartholemew the 2nd Jr Sr lost " + str(health_drop) + " fighting a monster!")
    counter += 1
    health = health - health_drop

#killing him
print("Aww, Jimmy Bartholemew the 2nd Jr Sr is drained of health! He survived " + str(counter) + " rounds.")

###########################################################################################################################################################

#set a counter
counter = 0

#make a list
orders = []

#make the loop with the input
while True:
    order = input("What would you like to order? (Type 'end' to finish): ")
    counter += 1
    #do the end
    if order == "end":
        break  #close the loop
    
    # put it in the list
    orders.append(order)

# Display the list of all the user's orders
print("Your orders:")
for item in orders:
    print(item)
