import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.instructions_label.pack(pady=10)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")  # Default choice

        choices = ["rock", "paper", "scissors"]

        for choice in choices:
            rb = tk.Radiobutton(root, text=choice, variable=self.user_choice_var, value=choice)
            rb.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: User - 0, Computer - 0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()  # Initially hidden

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"User: {user_choice}, Computer: {computer_choice}\nResult: {result}")
        
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        self.update_score()

        # Show play again button
        self.play_again_button.pack(pady=10)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self):
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def play_again(self):
        # Reset the result label and hide play again button
        self.result_label.config(text="")
        self.play_again_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
