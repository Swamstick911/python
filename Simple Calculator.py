#Making a Simple Calculator

print("Hello there user, this is a calculator")
print("Use '+' for addition '-' for subtraction '*' for multiplication and '/' for division")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = input("What operation would you like to do?:")

if operation == "+":
    sum = num1 + num2
    print(f'The sum is {sum}')
elif operation == "-":
    sub = num1 - num2
    print(f'The answer is {sub}')
elif operation == "*":
    product = num1 * num2
    print(f'The product is {product}')
elif operation == "/":
    div = num1 / num2
    print(f'The answer is {div}')


while True:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    operation = input("What operation would you like to do?:")

    if operation == "+":
        sum = num1 + num2
        print(f'The sum is {sum}')
    elif operation == "-":
        sub = num1 - num2
        print(f'The answer is {sub}')
    elif operation == "*":
        product = num1 * num2
        print(f'The product is {product}')
    elif operation == "/":
        div = num1 / num2
        print(f'The answer is {div}')



