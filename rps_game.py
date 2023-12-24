import random
from enum import Enum


def rps(name=''):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    player_icon = ""
    chosen_icon = False

    try:
        while True:
            first_exit = False

            class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSORS = 3
            
            def choose_icon():
                nonlocal chosen_icon
                nonlocal player_icon
                nonlocal first_exit

                while chosen_icon == False:
                    print(f'\n{name}, choose an icon\n1 for \U0001f600\n2 for \U0001F606\n3 for \U0001F923')

                    while True:
                        player_icon_choice = input('Enter number: ')
                        if player_icon_choice == 'q' or player_icon_choice == 'Q':
                            chosen_icon = True
                            first_exit = True
                            return
                        elif player_icon_choice.isdigit() == False:
                            print('Please enter a number')
                            break
                        else:
                            player_icon_num = int(player_icon_choice)

                            if player_icon_num == 1:
                                player_icon = "\U0001f600"
                                chosen_icon = True
                                return
                            elif player_icon_num == 2:
                                player_icon = "\U0001F606"
                                chosen_icon = True
                                return
                            elif player_icon_num == 3:
                                player_icon = "\U0001F923"
                                chosen_icon = True
                                return
                            else:
                                print('Please enter 1, 2, or 3')
            
            choose_icon()

            if first_exit == True:
                return

            print('----------------------------------------------------------------')
            print('WELCOME STUDENTS TO THE ROCK, PAPER, SCISSORS GAME MWHAHAHAHA!')

            print(f'\n{name} {player_icon}, please enter...\n1 for Rock\n2 for Paper\n3 for Scissor\n')


            while True:
                playerchoice = input('Enter number: ')
                if playerchoice == 'q' or playerchoice == 'Q':
                    return
                elif playerchoice.isdigit() == False:
                    print('Please enter 1, 2, or 3')
                    continue
                
                playernum = int(playerchoice)

                if playernum < 1 or playernum > 3:
                    print('Please enter 1, 2, or 3')
                else:
                    break
                

            computerchoice = random.choice("123")
            computernum = int(computerchoice)

            def game_logic(playernum, computernum):
                nonlocal game_count
                nonlocal player_wins
                nonlocal computer_wins

                game_count += 1

                if playernum == 1 and computernum == 3:
                    player_wins += 1
                    print(f"{player_icon}, you won! 🦄")
                elif playernum == 2 and computernum == 1:
                    player_wins += 1
                    print(f"{player_icon}, you won! 🦄")
                elif playernum == 3 and computernum == 2:
                    player_wins += 1
                    print(f"{player_icon}, you won! 🦄")
                elif playernum == computernum:
                    print( "It's a Tie")
                else:
                    computer_wins += 1
                    print(f"{player_icon}, you lost 💀")
                    

            print(f"\n{player_icon}, you chose: {str(RPS(playernum)).replace('RPS.', '')}")
            print(f"🐍 chose: {str(RPS(computernum)).replace('RPS.', '')}")
            game_mech = game_logic(playernum, computernum)

            print(f"\nGame count: {game_count}")
            if player_wins == 1:
                print(f"{player_icon} won {player_wins} time.")
            if player_wins > 1 or player_wins == 0:
                print(f"{player_icon} won {player_wins} times.")
            
            if computer_wins == 1:
                print(f"🐍 won {computer_wins} time.")
            if computer_wins > 1 or computer_wins == 0:
                print(f"🐍 won {computer_wins} times.")
            
            tie_num = game_count - (computer_wins+player_wins)
            print(f'🤝 Number of ties: {tie_num}')
            

            while True:
                print(f"\n{player_icon}, would you like to continue playing?\nType y for yes or q for quit")
                y_q = input()
                if y_q == 'y' or y_q == 'Y':
                    break
                elif y_q == 'q' or y_q == 'Q':
                    return
    finally:
        print('🎉🎉🎉 Thank you for playing! 🎉🎉🎉')

