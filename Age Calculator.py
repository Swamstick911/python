#Age Calculator

import datetime
import time
print("Hello User, this is an age calculator.")
print("Enter your name below")
name = input()

print(f"Hello {name}, Welcome to age calculator!")
time.sleep(1.5)
print("Enter the year in which you were born, below")
year = int(input())
currentYear = 2024

age = currentYear-year
print(f"{name} your age is {age}.")