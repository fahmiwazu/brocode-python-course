########## Deamon Thread

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for : ",count," seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)

answer = input("Do you want to exit?")