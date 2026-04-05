import random

def game():

    # Intro

    print("\n----- Welcome to Rock, Paper, Scissors Game -----\n")
    print("Rules: Rock beats Scissor | Scissor beats Paper | Paper beats Rock")
    print("Draw if both players select the same option.\n")

    name = input("What's your name?: ").capitalize()
    with open("Muzammil\score_board.txt") as f:
        score_board = f.read()

        if score_board == "":
            with open("Muzammil\score_board.txt", "a") as f:
                f.write(f'{name}: ')
        elif name not in score_board and score_board != "":
            with open("Muzammil\score_board.txt", "a") as f:
                f.write(f'\n{name}: ')

    # Computer & Your Choice

    options = ["Rock", "Scissor", "Paper"]
    pc_choice = random.choice(options).capitalize()

    ur_option = input(f"{name} choose an option (Rock/Paper/Scissor): ").capitalize()

    # Comparison

    if (ur_option != "Rock" or ur_option != "Paper" or ur_option != "Scissor"):
        print("\n❌ Invalid Input! Choose Rock, Paper, or Scissor.t")

    if (ur_option == pc_choice):
        print(f'\nPC Choose: {pc_choice} = You Choose: {ur_option}')
        print("Result: Draw 🤝")
        point = 0

    elif ((ur_option == "Rock" and pc_choice == "Scissor") or (ur_option == "Scissor" and pc_choice == "Paper") or (ur_option == "Paper" and pc_choice == "Rock")):
        print(f'\nPC Choose: {pc_choice} < You Choose: {ur_option}')
        print("Result: You WIN 🎉")
        point = 1

    else:
        print(f'\nPC Choose: {pc_choice} > You Choose: {ur_option}')
        print("Result: You LOSE 😢")
        point = -1

    if ((f'{name}: 1' in score_board) or (f'{name}: 0' in score_board) or (f'{name}: -1' in score_board)):
        with open("Muzammil\score_board.txt", "a") as f:
            f.write(f', {point}')
    else:
        with open("Muzammil\score_board.txt", "a") as f:
            f.write(f'{point}')

    # Asking Wanna Play Again

    ask = input("\nYou want to play again? (yes/no): ").lower()

    if ask == "yes":
        game()
    else:
        print("\nThanks for playing! Your final results are:")
        with open('Muzammil/score_board.txt') as f:
            print(f.read())


game()

