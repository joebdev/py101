def prompt(message):
    print(f'==> {message}')

prompt("Welcome to the Mortgage Calculator!")

# Make sure the input is a valid number
def invalid_num(number_str):
    try:
        num = float(number_str)
        if num <= 0:
            raise ValueError(f'Value must be > 0: {number_str}')
    except ValueError:
        return True
    return False

def mortgage_calculator():
    # Start with 'yes' to start process
    user_input = 'yes'
    # start a while loop, while user_input is yes run the code:
    while user_input == 'yes':
    # Ask the user for the loan price
        prompt("How much is your loan?")
        prompt("Example: 1_000_000 for 1000000")
        loan_amount = float(input())

        while invalid_num(loan_amount):
            prompt("Please enter a valid loan amount")
            loan_amount = float(input())

        # Find the APR <-- Get APR as a numerical value and
            # then divide it by 100 to get the percentage
        prompt("What is your interest rate?")
        prompt("Example: 5 for 5% or 7.5 for 7.5%")
        apr = (float(input())) / 100

        while invalid_num(apr):
            prompt("Please enter a valid APR")
            apr = float(input())

        # Find the length of the loan in years
        prompt("How many years is your loan?")
        loan_duration = float(input())

        while invalid_num(loan_duration):
            prompt("Please enter a valid number of years")
            loan_duration = float(input())

        # Take the duration in years and divide it by 12 to get the
            # monthly duration
        loan_duration_in_months = float(loan_duration) * 12

        # Divide the apr by 12 to get the monthly interest rate
        monthly_interest_rate = apr / 12

        # Calculate the monthly payment using the formula given
        monthly_payment = loan_amount * (
            monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (
                -loan_duration_in_months)))

        # Give the user the monthly amount
        print(f'Your monthly payment would be: ${round(monthly_payment, 2)}')

        # Ask the user if they would like to calculate another payment
        prompt('Would you like to calculate another payment?')

        # if the input is yes, it'll rerun, if anything else, exit
        user_input = input()

mortgage_calculator()