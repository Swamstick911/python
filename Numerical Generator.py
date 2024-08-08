
import random

print("Welcome to numerical generator!!")
print("Here you will get the numericals based on force and pressure")

difficulty = input("Choose your difficuty (easy, medium and  hard): ").lower()

def easy():
    print("You are in easy mode!")
    force = random.randint(0,150)
    pressure = random.randint(0,200)
    area = random.randint(0,100)
    missing = input("What will you find? (force, pressure, area): ").lower()

    if missing == "force":
        force = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming?  "))
        correctAnswer = round(pressure * area, 2)
        if answer == correctAnswer:
            print("Your answer is correct!")
        else:
            print("you're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    elif missing == "pressure":
        pressure = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming? "))
        correctAnswer = round(force / area, 2)
        if answer == correctAnswer:
            print("You're Correct!")
        else:
            print("You're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    elif missing == "area":
        area = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming? "))
        correctAnswer = round(force / pressure, 2)
        if answer == correctAnswer:
            print("You're correct!")
        else:
            print("You're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    else:
        print("Invalid Choice, try again!")
        easy()

def medium():
    print("You are in medium mode!")
    force = random.randint(0,300)
    pressure = random.randint(0,500)
    area = random.randint(0,200)
    missing = input("What will you find? (force, pressure, area): ").lower()

    if missing == "force":
        force = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming?  "))
        correctAnswer = round(pressure * area, 2)
        if answer == correctAnswer:
            print("Your answer is correct!")
        else:
            print("you're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    elif missing == "pressure":
        pressure = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming? "))
        correctAnswer = round(force / area, 2)
        if answer == correctAnswer:
            print("You're Correct!")
        else:
            print("You're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    elif missing == "area":
        area = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming? "))
        correctAnswer = round(force / pressure, 2)
        if answer == correctAnswer:
            print("You're correct!")
        else:
            print("You're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    else:
        print("Invalid Choice, try again!")
        medium()

def hard():
    print("You are in hard mode!")
    force = random.randint(0,1000)
    pressure = random.randint(0,10000)
    area = random.randint(0,200)
    missing = input("What will you find? (force, pressure, area): ").lower()

    if missing == "force":
        force = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming?  "))
        correctAnswer = round(pressure * area, 2)
        if answer == correctAnswer:
            print("Your answer is correct!")
        else:
            print("you're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    elif missing == "pressure":
        pressure = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming? "))
        correctAnswer = round(force / area, 2)
        if answer == correctAnswer:
            print("You're Correct!")
        else:
            print("You're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    elif missing == "area":
        area = "?"
        print(f"Force = {force} \nPressure = {pressure} \nArea = {area}")
        answer = float(input("What is your answer coming? "))
        correctAnswer = round(force / pressure, 2)
        if answer == correctAnswer:
            print("You're correct!")
        else:
            print("You're incorrect!")
            print(f"The correct answer was {correctAnswer}. ")
    else:
        print("Invalid Choice, try again!")
        hard()

if difficulty == "easy":
    easy()
elif difficulty == "medium":
    medium()
elif difficulty == "hard":
    hard()

