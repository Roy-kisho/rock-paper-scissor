import random

# points
user_points = 0
computer_points = 0



while computer_points != 3 or user_points != 3:
    # Computer choice 
    computer_choice = random.randint(1, 3);
    rock_paper_or_scissor = ""
    # checking whether computer choosed rock paper or scissor
    if computer_choice == 1:
        rock_paper_or_scissor = "rock"
    elif computer_choice == 2:
        rock_paper_or_scissor = "paper"
    elif computer_choice == 3:
        rock_paper_or_scissor = "scissor"
    
    # User choice
    user_choice = input("Enter Rock,Paper,Scissor to play or q to quit: ").lower()
    print(f"You played {user_choice}")
    print(f"Computer played {rock_paper_or_scissor}")

    # Game functions

    # When the game is tied
    if user_choice == "rock" and computer_choice == 1:
        print("Draw game try again")
    elif user_choice == "paper" and computer_choice == 2:
        print("Draw game try again")
    elif user_choice == "scissor" and computer_choice == 3:
        print("Draw game try again")
        
    # When user wins 
    elif user_choice == "rock" and computer_choice == 3:
        print("Congrats You won :)")
        user_points += 1
    elif user_choice == "paper" and computer_choice == 1:
        print("Congrats You won :)")
        user_points += 1
    elif user_choice == "scissor" and computer_choice == 2:
        print("Congrats You won :)")
        user_points += 1

    # When computer wins
    elif computer_choice == 1 and user_choice == "scissor":
        print("Oops Computer wins")
        computer_choice += 1
    elif computer_choice == 2 and user_choice == "rock":
        print("Oops Computer wins")
        computer_choice += 1
    elif computer_choice == 3 and user_choice == "paper":
        print("Oops Computer wins")
        computer_choice += 1
    elif user_choice == "q":
        print("Thank you for playing, come and play again :)")
        break
    else :
        print("You entered something behalf of Rock,Paper and Scissor :(")



print(f"User total points : {user_points}")
print(f"Computer total points : {computer_points}")