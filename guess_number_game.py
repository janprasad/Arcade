import random

def guess_number(name=''):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    quit_control = False

    try:
        while True:

            def gameplay():
                nonlocal game_count
                nonlocal player_wins
                nonlocal computer_wins
                nonlocal quit_control
                
                print('-------------------------------------------------')
                print(f"{name}, guess what number I am thinking of... 1, 2, or 3")

                while True:
                    player_choice = input('Enter number: ')
                    if player_choice == 'q' or player_choice == 'Q':
                        quit_control = True
                        return
                    elif player_choice.isdigit() == False:
                        print('Try again. Enter a number')
                        continue

                    player_choice_int = int(player_choice)

                    if player_choice_int < 1 or player_choice_int > 3:
                        print('Enter 1, 2, or 3')
                    else:
                        break
                
                computer_choice = random.choice('123')
                computer_choice_int = int(computer_choice)

                if computer_choice_int == player_choice_int:
                    game_count += 1
                    player_wins += 1
                    print(f'\n{name}, you chose {player_choice_int}')
                    print(f'I chose {computer_choice_int}')
                    print(f'{name}, you win!')
                else:
                    game_count += 1
                    computer_wins += 1
                    print(f'{name}, you chose {player_choice_int}')
                    print(f'I chose {computer_choice_int}')
                    print(f'{name}, you lost')
                
                print(f'\nGame count: {game_count}')
                print(f"Your wins: {player_wins}")

                percent_wins = str((player_wins/game_count)*100)+'%'
                print(f'Your winning percentage: {percent_wins}')

                while True:
                    print(f"\n{name}, would you like to continue playing?\nType y for yes or q for quit")
                    y_q = input()
                    if y_q == 'y' or y_q == 'Y':
                        break
                    elif y_q == 'q' or y_q == 'Q':
                        quit_control = True
                        return
            

            if quit_control == True:
                return
            
            gameplay()
    finally:
        print('🎉🎉🎉 Thank you for playing! 🎉🎉🎉')





