import random

# Scissors cuts Paper, Paper covers Rock, Rock
# crushes Lizard, Lizard poisons Spock, Spock
# smashes scissors, Scissors decapitates Lizard,
# Lizard eats paper, Paper disproves Spock,
# Spock vaporizes Rock, Rock crushes Scissors

# Scissors beats: Paper, Lizard     Loses to: Rock, Spock
# Paper beats: Rock, Spock          Loses to: Lizard, Scissors
# Rock beats: Lizard, Scissors      Loses to: Spock, Paper
# Lizard beats: Spock, Paper        Loses to: Scissors, Spock
# Spock beats: Scissors, Rock       Loses to: Paper, Lizard

# if ((player == 'rock' and computer == 'scissors') or
    #     (player == 'paper' and computer == 'rock') or
    #     (player == 'scissors' and computer == 'paper')):
    #     prompt('You win!')
    # elif ((player == 'rock' and computer == 'paper') or
    #     (player == 'paper' and computer == 'scissors') or
    #     (player == 'scissors' and computer == 'rock')):
    #     prompt('Computer wins!')
    # else:
    #     prompt("It's a tie!")


VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

def prompt(message):
    print(f'==> {message}')

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

player_score = 0
computer_score = 0

def display_winner(player, computer):
    global player_score
    global computer_score

    if computer in WINNING_COMBOS[player]:
        print('You win!')
        player_score += 1
    elif player in WINNING_COMBOS[computer]:
        print('Computer wins!')
        computer_score += 1
    else:
        print("It's a tie!")

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    player_choice = input()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        player_choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'''You chose {player_choice}, computer chose {computer_choice}''')

    display_winner(player_choice, computer_choice)

    prompt(f'Current score: You: {player_score}, Computer: {computer_score}')

    if player_score == 5 or computer_score == 5:
        player_score = 0
        computer_score = 0
        prompt('Do you want to play again? (y/n)?')
        answer = input().lower()
        while True:
            if answer.startswith('n') or answer.startswith('y'):
                break

            prompt('Please enter a "y" or "n".')
            answer = input().lower()

        if answer[0] == 'n':
            break
