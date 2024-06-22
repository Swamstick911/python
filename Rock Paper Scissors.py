 #Rock Paper Scissors

import random

print("Welcome to Rock, Paper, Scissors!")
print("What is your name?")
name = input()
print(f'Hello there {name}, lets start the rock paper scissors game')


def gameLoop():
    num = random.randint(1,3)
    user_choice = input("What will you choose (rock, paper, scissors): ").lower()

    if user_choice == "rock" and num == 1:
        print("I also chose rock, It's a draw!")
    elif user_choice == "rock" and num == 2:
        print("Yes! I chose paper, You lost!")
    elif user_choice == "rock" and num == 3:
        print("Oh no! I took Scissors, I lost!")
    elif user_choice == "paper" and num == 1:
        print("Oh no! I took rock, I lost!")
    elif user_choice == "paper" and num == 2:
        print("I also chose paper, It's a draw!")
    elif user_choice == "paper" and num == 3:
        print("Yes! I chose scissors, You lost!")
    elif user_choice == "scissors" and num == 1:
        print("Yes! I chose rock, You lost!")
    elif user_choice == "scissors" and num == 2:
        print("Oh no! I chose paper, I lost!")
    elif user_choice == "scissors" and num == 3:
        print("I also chose scissors, It's a draw!")
 
gameLoop()
