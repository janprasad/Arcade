from rps_game import rps
from guess_number_game import guess_number

def arcade(name=''):
    while True:
        print('-----------------------------------------------------')
        print(f"{name}, please choose a game:\n1: Rock, Paper, Scissors\n2: Guess the Number\n\nOr press 'x' to exit the game")

        user_input = input("\nEnter number: ")
        if user_input == 'x':
            print('🎉Thank you for coming to the arcade! See you soon! 🎉')
            return
        elif user_input.isdigit() == False:
            continue

        user_input_num = int(user_input)

        if user_input_num == 1:
            rps(name)
        elif user_input_num == 2:
            guess_number(name)
            


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Type the name of the person to greet"
    )

    args = parser.parse_args()

    arcade(args.name)