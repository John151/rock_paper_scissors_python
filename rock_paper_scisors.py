# Simple rock paper scissors program
import random

# Welcome message
print('Welcome to the Rock Paper Scissors game')

# number of games selected
number_of_rounds = 0
try:
    while number_of_rounds % 2 == 0 or number_of_rounds < 3 or number_of_rounds > 21 or type(number_of_rounds) != int:
        number_of_rounds = int(input('Please select an ODD number of rounds BETWEEN 3 and 21: '))
except ValueError:
    print('There has been an input error, please try again using only numbers, error')
except Exception as e:
    print('Something went wrong, please try again later.')
    print(e)

# declare some variables
# last user move
last_user_move = 0
current_round = 0
possible_moves = ['Rock', 'Paper', 'Scissors']
# user move selection input
# number of wins user has
user_score = 0
# number of wins computer has
computer_score = 0
# explanation of rules
print('For each round please make a choice between rock, paper, or scissors.\nTo play rock type \"1\"'
      '\nTo play paper type \"2\"\nTo play scissors type \"3\"')
# begin loop for however many games
while current_round < number_of_rounds:
    # ask user for input, rock paper or scissors
    user_move = int(input(f'Round {(current_round + 1)}:\n'
                          f'Current score is computer {computer_score} player: {user_score}\n'
                          f'Make your move (1 = rock, 2 = paper, or 3 = scissors): '))
    while type(user_move) != int or user_move < 1 or user_move > 3:
        user_move = int(input(f'It is still round {(current_round + 1)}:\n'
                              f'Make your move (1 = rock, 2 = paper, or 3 = scissors): '))
    print(f'User has chosen {possible_moves[(user_move - 1)]}')


# METHOD to determine computer move
# determine which strategy to use
# has strategy 2 or 3 been unsuccessful x times in a row? if yes skip

# is this the first match? if yes strategy 1

# strategy 1, choose move randomly
    computer_move = random.randint(1, 3)
    print(f'Computer has chosen {possible_moves[(computer_move -1)]}')
# strategy 2, case user just won, choose unplayed move

# strategy 3, case user just lost, choose user's last move

# METHOD to determine who won
    if user_move == computer_move: #user and computer tie
        print('tie, replay round')
    elif user_move == 1: #user selected rock
        if computer_move == 2: #computer selected paper
            print(f'Computer wins with {possible_moves[(computer_move - 1)]} beating {possible_moves[(user_move - 1)]}')
            current_round += 1
            computer_score += 1
        elif computer_move == 3: #computer selected scissors
            print(f'User wins with {possible_moves[(user_move - 1)]} beating {possible_moves[(computer_move - 1)]}')
            current_round += 1
            user_score += 1

    elif user_move == 2: #user selected paper
        if computer_move == 3: #computer selected scissors
            print(f'Computer wins with {possible_moves[(computer_move - 1)]} beating {possible_moves[(user_move - 1)]}')
            current_round += 1
            computer_score += 1
        elif computer_move == 1: #computer selected rock
            print(f'User wins with {possible_moves[(user_move - 1)]} beating {possible_moves[(computer_move - 1)]}')
            current_round += 1
            user_score += 1

    elif user_move == 3: #user selected scissors
        if computer_move == 1: #computer selected rock
            print(f'Computer wins with {possible_moves[(computer_move - 1)]} beating {possible_moves[(user_move - 1)]}')
            current_round += 1
            computer_score += 1
        elif computer_move == 2: #computer selected paper
            print(f'User wins with {possible_moves[(user_move - 1)]} beating {possible_moves[(computer_move - 1)]}')
            current_round += 1
            user_score += 1

# update scores, update information on how well strategies 2 and 3 are working

    last_user_move = user_move
# METHOD display:
# user has selected usermove
# computer has selected computermove
# who won, current score user: x computer: y games left: z
# if last game over, all results
