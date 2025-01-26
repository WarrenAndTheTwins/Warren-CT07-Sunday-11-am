print("Hello from lesson 2")

# using for loop, print out the following numbers

# 0 - 15
# for i in range(16):
#     print(i)
# 1 - 29
# for i in range(1, 30):
#     print(i)
# multiples of 4 from 4 to 48
# for i in range(4, 49, 4):
#     print(i)

# for loop --> you know exactly how many times to loop

# while loop --> repeating again and again, u do not know how many times to repeat.
# but you know when to stop

# for i in range(16):
#     print(i)

# count 1 - 15 using while loop

# count = 0
# while count < 16:
#     print(count)
#     count = count + 1
    # count += 1

# 1 - 29 (use the while loop)
# count = 1
# while count < 30:
#     print(count)
#     count += 1
# multiples of 5 from 5 to 60
# count = 5
# while count < 61:
#     print(count)
#     count += 5


# count = 10
# while count > 0:
#     print(count)
#     count -= 1

#     if count == 5:
#         print("Sad Half New Year! :(  ")
#         break
# else:
#     print("Happy New Year!")


# for i in range(10):
#     print(i)

#     if i == 5:
#         print("Half Happy!")
#         break
# else:
#     print("Happy!")

# remember the forever loop in scratch

# while True:
   
#     pw = input("What is your password? ")

#     if pw == "potatoman":
#         print("Access granted.")
#         break
#     else:
#         print("Intruder alert. Enter password again")
# price = 27.50
# import time
# import random
# delivery_time = random.randint(1,4)
# toppings_list = ""
# print("Welcome to Big Napoleon's")
# while True:
#     topping = input("What topping would you like? Type end to stop.")
#     if topping == "end":
#         if price > 0:
#             print("You have ordered a large pizza with " + toppings_list)
#             # print("That will be $" + str (price))
#             print(f'That will be ${price :.2f}, shipping and tax un-included')
#             while True:
#                 coupons = input("Do you have any coupons? Redeem them here. Say no to continue on and go directly to payment.")
#                 if coupons.lower() == "warren":
#                     price *= 0.75
#                     print(price)
#                     input("Alrighty. What's your Credit Card Number? We accept Visa, MasterCard, etc.")
#                     print("Delivery arriving soon.")
#                     for i in range(delivery_time,0,-1):
#                         print (str(i) + " more minutes till delivery.")
#                         time.sleep (60)
#                     print("Pizza delivered.")
#                     print("Time for another pizza!")
#                     toppings_list = ""
#                     price = 27.50
#                     delivery_time = random.randint(1,4)
#                     break

                    
#                 elif coupons.lower() == "shivermetimbers":
#                     price *= 0.90
#                     print(price)
#                     input("Alrighty. What's your Credit Card Number? We accept Visa, MasterCard, etc.")
#                     print("Delivery arriving soon.")
#                     for i in range(delivery_time,0,-1):
#                         print (str(i) + " more minutes till delivery.")
#                         time.sleep (60)
#                     print("Pizza delivered.")
#                     print("Time for another pizza!")
#                     toppings_list = ""
#                     price = 27.50
#                     delivery_time = random.randint(1,4)
#                     break
            

#                 else:
#                     input("Alrighty, either you entered an irredeemable code or don't have one. What's your Credit Card Number? We accept Visa, MasterCard, etc.")
#                     print("Delivery arriving soon.")
#                     for i in range(delivery_time,0,-1):
#                         print (str(i) + " more minutes till delivery.")
#                         time.sleep (60)
#                     print("Pizza delivered.")
#                     print("Time for another pizza!")
#                     toppings_list = ""
#                     price = 27.50
#                     delivery_time = random.randint(1,4)
#                     break
            
            
#         else: 
#             print("How are you gaining money????")
        
#     else:
#         toppings_list = toppings_list + topping +", "
#         if topping.lower() == "nuclear missiles":
#             price += 8400000
#         elif topping.lower() == "toyota corolla 2017":
#             price += 15500
#         elif topping.lower() == "honda civic 2025":
#             price += 30500
#         elif topping.lower() == "acura integra 2025":
#             price += 33000
#         elif topping.lower() == "Ultra1Plus Ultracool IAT Universal Antifreeze + Coolant Premixed 50/50 Green 1 us gallon":
#             price += 6.99
#         elif topping.lower() == "olives":
#             price += 1.5
#         elif topping.lower() == "pepperoni":
#             price += 1.75
#         elif topping.lower() == "ham":
#             price += 1.5
#         elif topping.lower() == "mushrooms":
#             price += 1.5
#         elif topping.lower() == "chicken":
#             price += 1.75
#         elif topping.lower() == "pineapple":
#             price += 2.5
#         elif topping.lower() == "charlie's flesh":
#             price += 12
#         elif topping.lower() == "turtle":
#             price += 30
#         else:
#             call = input("We don't serve that here. Would you like to make a special order for it?")
#             if call == "yes":
#                 print("BEEP BEEP...Call Connected")
#                 time.sleep(2.5)
#                 print("Hello! The robot said that you wanted to order " + topping + ". We might serve it here; let me double check...")
#                 time.sleep(3)
#                 print("DOO DA DOO DEEP DAT DO (hold music)")
#                 time.sleep(6)
#                 reasonable_price = input("Found it! How much is this, sir? I'm not quite sure. Name a reasonable price. DO NOT TYPE LETTERS.")
#                 if int(reasonable_price) <= 0:
#                     print("I'm sorry, I'm not giving you money; SCAMMER")
#                     time.sleep(2.5)
#                     print("BEEP BOOP. hangs up")
#                 else:
#                     price += int(reasonable_price)
#                     time.sleep(2) 
#                     print("beep boop. Call Ended")
            


'''
## Task 5: General Knowledge Quiz
**Task: Create a program to quiz users on their general
knowledge**

Using the while loop, ask 3 general knowledge questions
1. Using input ask the question
2. While answer is not correct, repeat the question.
3. Move on to the next question when the answer is correct

Bonus:
1. Add a score system
2. Add an ability for users to skip by saying “skip”
3. Disqualify user when they have tried too many times

'''
while True:
    ans = input("Gyatt rizz mew?")
    if ans == "chipi chipi chapa chapa".lower():
        print("Correct!")
        ans = input("What is the capital of Honduras?")
        if ans == "Tegucigalpa".lower():
            print("Correct!")
            ans = input("BIBI GOES BYE BYE")
            if ans == "I'M CRACKED WITH DYNAMIKE".lower():
                print("YOOO U CRACKED").lower()