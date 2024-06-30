#A number guessing game!
import random

print("Hello there user welcome to number guesssing game!")

difficulty = input("Please select a difficulty level: easy, medium, hard: ")

if difficulty == "easy":
  print("You have selected easy difficulty")
  number = random.randint(1,10)
  guess = int(input("Guess a number between 1 and 10: "))
  if guess == number:
    print("You guessed the number!")
  else:
    print("You did not guess the number")
    print(f"The number was {number} .")
elif difficulty == "medium":
  print("You have selected medium difficulty")
  number = random.randint(1,50)
  guess = int(input("Guess a number between 1 and 50: "))
  if guess == number:
    print("You guessed the number!")
  else:
    print("You did not guess the number")
    print(f"The number was {number} .")
elif difficulty == "hard":
  print("You have selected hard difficulty")
  number = random.randint(1,100)
  guess = int(input("Guess a number between 1 and 100: "))
  if guess == number:
    print("You guessed the number!")
  else:
    print("You did not guess the number")
    print(f"The number was {number} .")
