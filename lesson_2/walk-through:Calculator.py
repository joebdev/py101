# My solution BEFORE going through the walk-through video / text ------------------------

# print("Welcome to the command line calculator!")
# num1 = input("What is your first number? ")
# num2 = input("What is your second number? ")
# operation = input("Want to add, subtract, multiply, or divide? ")

# match operation:
#     case 'add':
#         print(f'{int(num1)} + {int(num2)} = {int(num1) + int(num2)}')
#     case 'subtract':
#         print(f'{int(num1)} - {int(num2)} = {int(num1) - int(num2)}')
#     case 'multiply':
#         print(f'{int(num1)} * {int(num2)} = {int(num1) * int(num2)}')
#     case 'divide':
#         print(f'{int(num1)} / {int(num2)} = {int(num1) // int(num2)}')

# Walk-Through Solution-----------------------------------------------------
# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the results to the terminal

print("Welcome to Calculator!")

print("What's the first number?")
num1 = int(input())
print("What's the second number?")
num2 = int(input())

print("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

if operation == '1': # '1' represents addition
    output = num1 + num2
elif operation == '2': # '2' represents subtraction
    output = num1 - num2
elif operation == '3': # '3' represents multiplication
    output = num1 * num2
elif operation == '4': # '4' represents division
    output = num1 // num2
else:
    print("That's not an operator, try again!")

print(f'The result is: {output}')