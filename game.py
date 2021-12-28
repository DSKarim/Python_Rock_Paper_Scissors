import random

possible_choices = ['rock', 'paper', 'scissors']


def who_won(player, computer):
    """
    This function determines the winner of the game.
    """
    if player == computer:
        return 'tie'
    else:
        player_index = possible_choices.index(player)
        win_lose_list = possible_choices[player_index + 1:] + possible_choices[:player_index]
        if win_lose_list.index(computer) + 1 <= len(win_lose_list) // 2:
            return 'computer'
        else:
            return 'player'


user_name = input("Enter your name:")
print("Hello, " + user_name)
user_rating = 0

with open("rating.txt") as file:
    for line in file:
        if user_name == line.rstrip().split()[0]:
            user_rating = int(line.rstrip().split()[1])

user_possible_choices = input()
if user_possible_choices != "":
    possible_choices = user_possible_choices.split(",")
print("Okay, let's start")

while True:
    user_choice = input()
    if user_choice not in possible_choices:
        if user_choice == '!exit':
            print('Bye!')
            break
        elif user_choice == '!rating':
            print('Your rating:', user_rating)
        else:
            print('Invalid input')
    else:
        computer_choice = random.choice(possible_choices)

        result = who_won(user_choice, computer_choice)
        if result == 'player':
            print('Well done. The computer chose {option} and failed'.format(option=computer_choice))
            user_rating += 100
        elif result == 'computer':
            print('Sorry, but the computer chose {option}'.format(option=computer_choice))
        elif result == 'tie':
            print('There is a draw ({option})'.format(option=computer_choice))
            user_rating += 50
