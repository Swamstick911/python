#A Quiz Generator

import time
print("Hello there, welcome to quiz generator!")
time.sleep(2)
print("What kinda quiz you wanna generate? (Science or GK)")
type = input().lower()

def science():
    print("Welcome to Science Quiz!!")
    time.sleep(2)
    print("Who is known as the father of chemistry? ")
    answer1 = input().lower()
    print("What is the powerhouse of cell?")
    answer2 = input().lower()
    print("What is the basic unit of life? ")
    answer3 = input().lower()
    if answer1 == "antoine lavoisier":
        print("You're correct!")
    else:
        print("You're incorrect!")
        print("Correct answer is Antoine Lavoisier")
    if answer2 == "mitochondria":
        print("You're correct!")
    else:
        print("You're incorrect! \nCorrect Answer is Mitochondria")
    if answer3 == "cell":
        print("You're correct!")
    else:
        print("You're incorrect! \nCorrect answer is cell.")


    
def gk():
    print("Welcome to GK Quiz!!")
    time.sleep(2)
    print("What is the capital of France? ")
    answer1 = input().lower()
    print("What is the largest ocean in the world?")
    answer2 = input().lower()
    print("What is the smallest country in the world by land area? ")
    answer3 = input().lower()
    if answer1 == "paris":
        print("You're correct!")
    else:
        print("You're incorrect!")
        print("Correct answer is Paris")
    if answer2 == "pacific" or "pacific ocean":
        print("You're correct!")
    else:
        print("You're incorrect! \nCorrect Answer is Pacific Ocean")
    if answer3 == "vatican city":
        print("You're correct!")
    else:
        print("You're incorrect! \nCorrect answer is Vatican City")
    

def choice():
    if type == "science":
        science()
    elif type == "gk":
        gk()
    else:
        print("Invalid choice try again!")
        choice()

choice()
