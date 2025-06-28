import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Game state variables
user_score = 0
computer_score = 0

# Functions
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissor') or \
         (user == 'scissor' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def play(user_choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

    if winner == 'tie':
        result_text += "It's a tie!"
    elif winner == 'user':
        user_score += 1
        result_text += "You win! 🎉"
    else:
        computer_score += 1
        result_text += "You lose! 💻"

    result_label.config(text=result_text)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text="Score: You 0 - 0 Computer")

# GUI Widgets
title_label = tk.Label(root, text="🪨📄✂️ Rock-Paper-Scissor Game ✂️📄🪨", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
scissors_button = tk.Button(button_frame, text="Scissor", width=10, command=lambda: play("scissor"))

rock_button.grid(row=0, column=0, padx=10, pady=5)
paper_button.grid(row=0, column=1, padx=10, pady=5)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Helvetica", 12), bg="#f0f0f0")
score_label.pack(pady=20)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Run the GUI
root.mainloop()
