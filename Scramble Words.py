# Word Scramble game

import random

print("Welcome to the Scramble game!!")
print("How many rounds would you like to play!")
rounds = int(input())

words = ["python", "ultra", "program", "eat", "seat", "scramble", "rickroll", "game"]

def scrambleWord(words):
    word = list(words)
    random.shuffle(word)
    return ''.join(word)

def gameLoop():
    score = 0
    for _ in range(rounds):
        word = random.choice(words)  # Pick a random word from the list
        scrambled = scrambleWord(word)
        print(f"Scrambled word: {scrambled}")
        
        guess = input("Your guess: ")
        
        if guess.lower() == word.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct word was {word}.")
        
        print()  
    
    print(f"Game Over! Your final score is {score} out of {rounds}.")

gameLoop()

