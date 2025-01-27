import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt(MESSAGES['welcome'])

def run_calculator():
    user_answer = 'yes'
    while user_answer == 'yes' or str == 'Yes':
        prompt(MESSAGES['first'])
        num1 = input()

        while invalid_number(num1):
            prompt(MESSAGES['invalid_number'])
            num1 = input()

        prompt(MESSAGES['second'])
        num2 = input()

        while invalid_number(num2):
            prompt(MESSAGES['invalid_number'])
            num2 = input()


        prompt(MESSAGES['operation'])
        operation = input()

        while operation not in ['1', '2', '3', '4']:
            prompt(MESSAGES['operation_error'])
            operation = input()

        match operation:
            case '1': # '1' represents addition
                output = float(num1) + float(num2)
            case '2': # '2' represents subtraction
                output = float(num1) - float(num2)
            case '3': # '3' represents multiplication
                output = float(num1) * float(num2)
            case '4': # '4' represents division
                output = float(num1) / float(num2)


        prompt(f'The result is: {output}')
        prompt(MESSAGES['restart'])
        user_answer = input()

run_calculator()