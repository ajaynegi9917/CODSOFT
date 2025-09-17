import random

def play_game():
    """
    This function contains the main logic for a single round of Rock-Paper-Scissors.
    """
    
    # 1. Get User Input
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Validate user input
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
    # 2. Generate Computer's Choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Display the choices
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}\n")
    
    # 3. Determine the Winner
    # 4. Display the Result
    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"

# Main program loop
def main():
    """
    This function manages the score tracking and the "play again" loop.
    """
    user_score = 0
    computer_score = 0
    
    while True:
        result = play_game()
        
        # Update scores based on the result
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
            
        print(f"\nCurrent Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

# Run the main program
if __name__ == "__main__":
    main()
