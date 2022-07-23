import random


# points
user_points = 0
computer_points = 0

while user_points != 3 and computer_points != 3:

    # Computer choice
    random_num = random.randint(1, 3)
    computer_choice = ""

    # checking whether computer choosed rock paper or scissor
    if random_num == 1:
        computer_choice = "r"
    elif random_num == 2:
        computer_choice = "p"
    elif random_num == 3:
        computer_choice = "s"

    # User choice
    user_choice = input(
        "Enter (r)ock,(p)aper, (s)cissor to play or q to quit: ").lower()

    if user_choice == 'r' or user_choice == 's' or user_choice == 'p' or user_choice == 'q':
        # Game functions

        # When the game is tied
        if user_choice == computer_choice:
            if user_choice == 'r':
                print("Rock vs Rock")
            elif user_choice == 'p':
                print("Paper vs Paper")
            elif user_choice == 's':
                print("Scissor vs Scissor")
            print("Game Draw 😬")
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
        # When user wins
        elif user_choice == "r" and computer_choice == 's':
            print("Rock Vs Scissor")
            print("You won 😉")
            user_points += 1
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
        elif user_choice == "p" and computer_choice == 'r':
            print("Paper Vs Rock")
            print("You won 😉")
            user_points += 1
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
        elif user_choice == "s" and computer_choice == 'p':
            print("Scissor Vs Paper")
            print("You won 😉")
            user_points += 1
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")

        # When computer wins
        elif user_choice == "s" and computer_choice == 'r':
            print("Scissor Vs Rock")
            print("You lose 😕")
            computer_points += 1
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
        elif user_choice == "r" and computer_choice == 'p':
            print("Rock Vs Paper")
            print("You lose 😕")
            computer_points += 1
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
        elif user_choice == "p" and computer_choice == 's':
            print("Paper Vs Scissor")
            print("You lose 😕")
            computer_points += 1
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
        elif user_choice == "q":
            print(f"Player points : {user_points}")
            print(f"Ai points : {computer_points}")
            break
    else:
        print("""
r -> Rock
p -> paper
s -> Scissor
""")

if user_points > computer_points:
    print("Awesome you won the game 🕺")
elif computer_points > user_points:
    print("Oops you lost the game, better luck next time 🙂.")
