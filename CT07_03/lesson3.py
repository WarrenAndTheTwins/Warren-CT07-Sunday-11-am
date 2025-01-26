print("Hello from lesson 3")

import time

timer = input("how long is ur study time?")
while timer > 0:
    print (timer)
    time.sleep(60)
    timer -= 1
print()