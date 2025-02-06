# print("Hello from lesson 3")
# timer = 1
# import time

# int(timer) == input("how long is ur study time?")
# while timer > 0:
#     print (timer)
#     time.sleep(60)
#     timer -= 1
# print("U dumdum, so keep studying.")

savings = 0
while savings < 100:
    savings_today = input("How much you save today?")
    savings = savings + float(savings_today)
print("U suck. Noone likes u. Your free trial has ended, now you must pay " + str(savings) + " dollars.")
