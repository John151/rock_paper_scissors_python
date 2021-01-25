# Simple rock paper scissors program
import random

# Welcome message
print('Welcome to the Rock Paper Scissors game')

# number of games selected
possible_moves = ('Rock', 'Paper', 'Scissors')


def main():
    number_of_rounds = determine_number_rounds()

    # moves from previous round
    last_user_move = 0
    last_computer_move = 0
    # winner of last round
    computer_won_last_round = False

    current_round = 0
    # number of wins user has
    user_score = 0
    # number of wins computer has
    computer_score = 0
    # explanation of rules
    print('For each round please make a choice between rock, paper, or scissors.\nTo play rock type \"1\"'
          '\nTo play paper type \"2\"\nTo play scissors type \"3\"')
    while current_round < number_of_rounds:
        computer_move = determine_computer_move(last_user_move, last_computer_move, computer_won_last_round)
        user_move = determine_user_move(current_round, computer_score, user_score)
        last_user_move = user_move
        last_computer_move = computer_move
        determine_outcome(user_move, computer_move, current_round, computer_score, user_score)

    print(f'Final scores:\nComputer: {computer_score} wins\nUser: {user_score} wins')

def determine_number_rounds():
    try:
        number_of_rounds = 0
        while number_of_rounds % 2 == 0 or number_of_rounds < 3 or number_of_rounds > 21 or type(number_of_rounds) != int:
            number_of_rounds = int(input('Please select an ODD number of rounds BETWEEN 3 and 21: '))
        return number_of_rounds
    except ValueError:
        print('There has been an input error, please try again using only numbers, error')
    except Exception as e:
        print('Something went wrong, please try again later.')
        print(e)


def determine_user_move(current_round, computer_score, user_score):

    # ask user for input, rock paper or scissors
    user_move = int(input(f'Round {(current_round + 1)}:\n'
                          f'Current score is computer {computer_score} player: {user_score}\n'
                          f'Make your move (1 = rock, 2 = paper, or 3 = scissors): '))
    while type(user_move) != int or user_move < 1 or user_move > 3:
        user_move = int(input(f'It is still round {(current_round + 1)}:\n'
                              f'Make your move (1 = rock, 2 = paper, or 3 = scissors): '))
    print(f'User has chosen {possible_moves[(user_move - 1)]}')
    return user_move

def determine_computer_move(last_user_move, last_computer_move, computer_won_last_round):

    # METHOD to determine computer move
    # determine which strategy to use

    # has there been a match? if yes we will use the data to predict the next move

    if last_user_move and computer_won_last_round:
        # strategy 1, case user just lost, choose user's last move
        computer_move = last_user_move

    elif last_user_move and not computer_won_last_round:
        # strategy 2, case user just won, choose unplayed move
        for choice in range(1, 4):
            if choice != last_computer_move and choice != last_user_move:
                computer_move = choice
    # strategy 3, choose move randomly
    else:
        computer_move = random.randint(1, 3)

    return computer_move


# METHOD to determine who won
def determine_outcome(user_move, computer_move, current_round, computer_score, user_score):
    if user_move == computer_move:  # user and computer tie
        print('tie, replay round')
    elif user_move == 1:  # user selected rock
        if computer_move == 2:  # computer selected paper
            print(f'Computer wins with {possible_moves[(computer_move - 1)]} beating {possible_moves[(user_move - 1)]}')
            current_round += 1
            computer_score += 1
        elif computer_move == 3:  # computer selected scissors
            print(f'User wins with {possible_moves[(user_move - 1)]} beating {possible_moves[(computer_move - 1)]}')
            current_round += 1
            user_score += 1

    elif user_move == 2:  # user selected paper
        if computer_move == 3:  # computer selected scissors
            print(f'Computer wins with {possible_moves[(computer_move - 1)]} beating {possible_moves[(user_move - 1)]}')
            current_round += 1
            computer_score += 1
        elif computer_move == 1:  # computer selected rock
            print(f'User wins with {possible_moves[(user_move - 1)]} beating {possible_moves[(computer_move - 1)]}')
            current_round += 1
            user_score += 1

    elif user_move == 3:  # user selected scissors
        if computer_move == 1:  # computer selected rock
            print(f'Computer wins with {possible_moves[(computer_move - 1)]} beating {possible_moves[(user_move - 1)]}')
            current_round += 1
            computer_score += 1
        elif computer_move == 2:  # computer selected paper
            print(f'User wins with {possible_moves[(user_move - 1)]} beating {possible_moves[(computer_move - 1)]}')
            current_round += 1
            user_score += 1


main()
