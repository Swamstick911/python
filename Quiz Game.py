# Quiz Game
import time
import random

print("Hello and welcome to quiz game!")
print("Please enter your name")
name = input()

print(f"Hello there {name}, lets start our quiz!")
print("There will be 5 questions in the quiz")
time.sleep(5)
print("Lets Start!")

ques1 = random.randint(1,5)
ques2 = random.randint(1,5)
ques3 = random.randint(1,5)
ques4 = random.randint(1,5)
ques5 = random.randint(1,5)
score = 0

if ques1 == 1:
    print("First question, Who is the Richest person in the world?")
    answer1 = input().lower()
    if answer1 ==  "bernard arnault":
        score += 1
    else:
        score -= 1
elif ques1 == 2:
    print("First question, What is 2 to the power of 5?")
    answer1 = input().lower()
    if answer1 ==  "32":
        score += 1
    else:
        score -= 1
elif ques1 == 3:
    print("First question, Who is the president of USA?")
    answer1 = input().lower()
    if answer1 ==  "joe biden":
        score += 1
    else:
        score -= 1
elif ques1 == 4:
    print("First question, Who is the owner of tesla?")
    answer1 = input().lower()
    if answer1 ==  "elon musk":
        score += 1
    else:
        score -= 1
elif ques1 == 5:
    print("First question, Smallest continent by land?")
    answer1 = input().lower()
    if answer1 ==  "australia":
        score += 1
    else:
        score -= 1

if ques2 == 1:
    print("Second question, What is the currency of Japan?")
    answer2 = input().lower()
    if answer2 ==  "yen":
        score += 1
    else:
        score -= 1
elif ques2 == 2:
    print("Second question, What is the capital of france?")
    answer2 = input().lower()
    if answer2 ==  "paris":
        score += 1
    else:
        score -= 1
elif ques2 == 3:
    print("Second question, Largest planet in our solar system")
    answer2 = input().lower()
    if answer2 ==  "jupiter":
        score += 1
    else:
        score -= 1
elif ques2 == 4:
    print("Second question, What is the longest river in the world?")
    answer2 = input().lower()
    if answer2 ==  "nile":
        score += 1
    else:
        score -= 1
elif ques2 == 5:
    print("Second question, Who was the first man to walk on the moon? (full name)")
    answer2 = input().lower()
    if answer2 ==  "neil armstrong":
        score += 1
    else:
        score -= 1


if ques3 == 1:
    print("Third question, Fastest Animal on Earth?")
    answer3 = input().lower()
    if answer3 ==  "cheetah":
        score += 1
    else:
        score -= 1
elif ques3 == 2:
    print("Third question, Tallest mountain in the world?")
    answer3 = input().lower()
    if answer3 ==  "mount everest":
        score += 1
    else:
        score -= 1
elif ques3 == 3:
    print("Third question, Hardest natural substance?")
    answer3 = input().lower()
    if answer3 ==  "diamonds":
        score += 1
    else:
        score -= 1
elif ques3 == 4:
    print("Third question, First president of USA? (full name)")
    answer3 = input().lower()
    if answer3 ==  "george washington":
        score += 1
    else:
        score -= 1
elif ques3 == 5:
    print("Third question, Hottest planet in the solar system?")
    answer3 = input().lower()
    if answer3 ==  "venus":
        score += 1
    else:
        score -= 1

if ques4 == 1:
    print("Fourth question, Largest ocean in the world?")
    answer4 = input().lower()
    if answer4==  "pacific":
        score += 1
    else:
        score -= 1
elif ques4 == 2:
    print("Fourth question, Currency of India?")
    answer4 = input().lower()
    if answer4 ==  "rupees":
        score += 1
    else:
        score -= 1
elif ques4 == 3:
    print("Fourth question, Smallest country by land area?")
    answer4 = input().lower()
    if answer4 ==  "vatican city":
        score += 1
    else:
        score -= 1
elif ques4 == 4:
    print("Fourth question, Largest desert in the world?")
    answer4 = input().lower()
    if answer4 ==  "sahara":
        score += 1
    else:
        score -= 1
elif ques4 == 5:
    print("Fourth question, Country with most olympic gold medals?")
    answer4 = input().lower()
    if answer4 ==  "usa":
        score += 1
    else:
        score -= 1

if ques5 == 1:
    print("Fifth question, Longest bone in human body?")
    answer5 = input().lower()
    if answer5 ==  "femur":
        score += 1
    else:
        score -= 1
elif ques5 == 2:
    print("Fifth question, City known as big apple?")
    answer5 = input().lower()
    if answer5 ==  "new york":
        score += 1
    else:
        score -= 1
elif ques5 == 3:
    print("Fifth question, Most populous country?")
    answer5 = input().lower()
    if answer5 ==  "india":
        score += 1
    else:
        score -= 1
elif ques5 == 4:
    print("Fifth question, Largest island?")
    answer5 = input().lower()
    if answer5 ==  "greenland":
        score += 1
    else:
        score -= 1
elif ques5 == 5:
    print("Fifth question, Capital of Canada")
    answer5 = input().lower()
    if answer5 ==  "ottawa":
        score += 1
    else:
        score -= 1

print(f"{name}, your score is {score}!")