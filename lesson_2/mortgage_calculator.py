import os
import math

def prompt(message):
    print(f'===> {message}')

# Check to make sure the input is a valid number greater than 0,
    # not inf, not nan
def invalid_num(number_str):
    try:
        num = float(number_str)
        if num <= 0 or math.isnan(num) or num == float('inf'):
            raise ValueError(f'Value must be > 0: {number_str}')
    except ValueError:
        return True
    return False

# Function to get the loan amount, check for validity,
    #  and return the loan amount
def find_loan_amount():
    prompt("How much is  your loan?")
    prompt("Example: 1_000_00 for 1000000")
    loan_amount = input()
    while invalid_num(loan_amount):
        prompt("Please enter a valid loan amount, don't use nan or inf")
        loan_amount = input()
    return loan_amount

# Function to get the apr, check for validity,
    #  and return the apr
def find_apr():
    prompt("What is your interest rate?")
    prompt("Example: 5 for 5% or 7.5 for 7.5%")
    apr = input()
    while invalid_num(apr):
        prompt("Please enter a valid interest rate")
        apr = input()
    return apr

# Function to get the loan duration, check for validity,
    #  and return the loan duration
def find_loan_duration():
    prompt("How many years is your loan?")
    loan_duration = input()
    while invalid_num(loan_duration):
        prompt("Please enter a valid number of years")
        loan_duration = input()
    return loan_duration

# Function to get calculate the monthly payment,
    # check for validity, and return payment amount
def calculate_monthly_payment():
    price_of_loan = float(find_loan_amount())
    loan_duration_in_months = float(find_loan_duration()) * 12
    annual_interest_rate = float(find_apr()) / 100
    monthly_interst_rate = annual_interest_rate / 12

    monthly_payment = float(price_of_loan) * (
        monthly_interst_rate / (1 - (1 + monthly_interst_rate) ** (
            -loan_duration_in_months
        ))
    )

    print(f'Your monthly payment would be: ${round(monthly_payment, 2)}')

# Runs the calculator, and checks after each time to see if user would like
    # to continue with another calculation or not
def run_calculator():
    user_input = "yes"
    while user_input[0] == "y":
        os.system('clear')
        calculate_monthly_payment()
        prompt('Would you like to calculate another payment?')
        prompt('Please enter "yes" or "no".')
        user_input = input().lower()
        if user_input[0] != "y":
            break

run_calculator()