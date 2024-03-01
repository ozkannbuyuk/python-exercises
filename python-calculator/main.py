import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Division by zero error")
        return 0
    else:
        return a / b

def power(a, b):
    return a ** b

while True:
    os.system('cls')
    print("""
    *** CRAZY CALCULATOR ***
    
            1- ADDITION
            2- SUBTRACTION
            3- MULTIPLICATION
            4- DIVISION
            5- POWER
    """)
    choice = input("YOUR CHOICE:")
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")

    if choice == "1":
        print(add(int(num1), int(num2)))
    elif choice == "2":
        print(subtract(int(num1), int(num2)))
    elif choice == "3":
        print(multiply(int(num1), int(num2)))
    elif choice == "4":
        print(divide(int(num1), int(num2)))
    elif choice == "5":
        print(power(int(num1), int(num2)))
    else:
        print("Invalid operation")
    input("Press ENTER to continue...")
