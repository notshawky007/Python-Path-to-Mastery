import random

class RockPaperScissorsGame:
    """
    Rock-Paper-Scissors game class.
    """

    def __init__(self):
        """
        Initialize the game with choices and their winning conditions.
        """
        self.choices = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }

    def get_user_choice(self):
        """
        Get and validate the user's choice.
        """
        while True:
            user_input = input("Enter your choice (rock, paper, scissors): ").lower()
            if user_input in self.choices:
                return user_input
            print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        """
        Randomly select the computer's choice.
        """
        return random.choice(list(self.choices.keys()))

    def determine_winner(self, user_choice, computer_choice):
        """
        Determine the winner based on choices.
        """
        if user_choice == computer_choice:
            return "It's a tie!"
        elif self.choices[user_choice] == computer_choice:
            return "You win!"
        else:
            return "You lose!"

    def play_again(self):
        """
        Ask the user if they want to play again.
        """
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                return play_again == 'yes'
            print("Invalid input. Please enter 'yes' or 'no'.")

    def play_game(self):
        """
        Start and manage the game loop.
        """
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            print(self.determine_winner(user_choice, computer_choice))
            
            if not self.play_again():
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()