#Question 1 - Make a Hello World program
print("Hello World!")

#Question 2 - Make a program with variable that assigns your name and then prints it
name = "Swastik Bajpai"
print(name)

#Question 3 - Do Simple Arithmetic 
print(2 + 6)
print(6 - 2)
print(2 / 6)
print(2 * 6)
print(2 % 6)

#Question 4 - Write a program that checks if a number entered by the user is even or odd and prints an appropriate message.
num = int(input("Enter a number: "))


if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Question 5 - Write a program that prints the numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

#Question 6 - Create a list of your favorite fruits and print each fruit using a for loop.

favourite_fruits = ["apple", "banana", "mango", "orange"]
for fruits in favourite_fruits:
    print(fruits)

#Question 7 - Write a function called greet that takes a name as an argument and prints "Hello, [name]!".

name = input("Enter your name: ")
def greet():
    print(f"Hello {name}")

greet()

#Question 8 - Create a dictionary with the names and ages of three people. Print each name and age in a formatted string.

people_ages = {
    "Alice" : 24,
    "Bard" : 41,
    "Carl" : 17
}

for name, ages in people_ages.items():
    print(f"{name} is {age} years old!")

    