def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt("Welcome to Calculator!")

prompt("What's the first number?")
num1 = input()

while invalid_number(num1):
    prompt('Hmm... that doesnt look like a valid number.')
    num1 = input()

prompt("What's the second number?")
num2 = input()

while invalid_number(num2):
    prompt('Hmm... that doesnt look like a valid number.')
    num2 = input()


prompt('''What operation would you like to perform?
       1) Add 2) Subtract 3) Multiply 4) Divide''')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case '1': # '1' represents addition
        output = int(num1) + int(num2)
    case '2': # '2' represents subtraction
        output = int(num1) - int(num2)
    case '3': # '3' represents multiplication
        output = int(num1) * int(num2)
    case '4': # '4' represents division
        output = int(num1) / int(num2)


prompt(f'The result is: {output}')