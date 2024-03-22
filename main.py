import random

# create a game rock, paper, scissors
# the game will be played 3 times between the user and the computer
# the user will be asked to enter their choice
# the computer will randomly select a choice
# the winner will be declared after each round
# the overall winner will be declared after 3 rounds
# the user will be asked if they want to play again
# if the user selects yes, the game will start again
# if the user selects no, the game will end
def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    for _ in range(3):
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print("\n--- Game Over ---")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < computer_score:
        print("Sorry! Computer is the overall winner!")
    else:
        print("It's a tie!")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == 'yes':
            play_game()
        elif choice.lower() == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

play_game()
play_again()

