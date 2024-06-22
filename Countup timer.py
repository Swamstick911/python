#A countup timer

import time

print("Hello there user, This is a countdown timer!")
seconds = int(input("Please input the time in seconds: "))

def countdown():
    for i in range(seconds):
        print(i + 1)
        time.sleep(1)

countdown()
