

import time
import random

def easyMode():
    print("You entered Easy mode")
    time.sleep(2)
    num = random.randint(1,20)
    print("I am thinking of a number between 1-20...")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You're correct")
    else:
        print("You're incorrect")

def intermediate():
    print("You entered intermediate mode")
    time.sleep(2)
    num = random.randint(1,40)
    print("I am thinking of a number between 1-40...")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You are correct!")
    else:
        print("You are incorrect!")

def medium():
    print("You entered medium mode")
    time.sleep(2)
    num = random.randint(1,50)
    print("I am thinking of a number between 1-50...")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You're correct!")
    else:
        print("You're incorrect!")

def hard():
    print("You entered hard mode")
    time.sleep(2)
    num = random.randint(1, 100)
    print("I am thinking of a number between 1-100...")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You are correct!")
    else:
        print("You are incorrect!")

def ultraHard():
    print("You entered Ultra Hard Mode")
    time.sleep(2)
    num = random.randint(1, 150)
    print("I am thinking of a number between 1-150...")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You're correct!")
    else:
        print("You're incorrect!")

def insane():
    print("You entered insane mode")
    time.sleep(2)
    num = random.randint(1, 500)
    print("I am thing of a number between 1-200")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You're correct!")
    else:
        print("You're incorrect!")

def god():
    print("You entered the god mode")
    time.sleep(2)
    num = random.randint(1,1000)
    print("I am thinking of a number between 1-1000")
    time.sleep(2)
    print("Guess the number")
    guess = int(input())
    if guess == num:
        print("You're correct!")
    else:
        print("You're incorrect!")


print("Hello there, Welcome to Number Guessing game!")
name = input("Enter you name please: ")

print(f"Hello {name}, What mode would you like to play? (easy, intermediate, medium, hard, ultra hard, insane, god)")
difficulty = input().lower()


def choice():
    if difficulty == "easy":
        easyMode()
    elif difficulty == "intermediate":
        intermediate()
    elif difficulty == "medium":
        medium()
    elif difficulty == "hard":
        hard()
    elif difficulty == "ultra hard":
        ultraHard()
    elif difficulty == "insane":
        insane() 
    elif difficulty == "god":
        god()
    else:
        print("Invalid choice please try again!")
        choice()
