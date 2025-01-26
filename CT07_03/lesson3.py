print("Hello from lesson 3")

import time

timer = input("how long is ur study time?")
while int(timer) > 0:
    print (timer)
    time.sleep(60)
    int(timer) -= 1
print("U dumdum, so keep studying.")