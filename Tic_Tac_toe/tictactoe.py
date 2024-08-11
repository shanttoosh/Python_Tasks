import tkinter as tk
from tkinter import messagebox

# Setting up the environment
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

# Creating grid
buttons = [[None, None, None], [None, None, None], [None, None, None]]

current_player = "X"
winner_buttons = []

# Handling moves
def click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and check_winner() is False:
        buttons[row][col]["text"] = current_player
        winner = check_winner()
        if winner is False:
            current_player = "O" if current_player == "X" else "X"
            update_status()
        elif winner is True:
            highlight_winner()
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            show_restart_button()
        elif winner == "Tie":
            highlight_tie()
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            show_restart_button()

def check_winner():
    global winner_buttons
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            winner_buttons = [(row, 0), (row, 1), (row, 2)]
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            winner_buttons = [(0, col), (1, col), (2, col)]
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        winner_buttons = [(0, 0), (1, 1), (2, 2)]
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        winner_buttons = [(0, 2), (1, 1), (2, 0)]
        return True
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return "Tie"

def highlight_winner():
    for (row, col) in winner_buttons:
        buttons[row][col].config(bg="lightgreen")

def highlight_tie():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(bg="lightyellow")

def reset_game():
    global current_player, winner_buttons
    current_player = "X"
    winner_buttons = []
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="SystemButtonFace")
    restart_button.grid_remove()
    update_status()

def show_restart_button():
    restart_button.grid(row=4, column=0, columnspan=3, pady=10)

def update_status():
    status_label.config(text=f"Current Player: {current_player}")

# Creating buttons and status label
status_label = tk.Label(root, text=f"Current Player: {current_player}", font=('normal', 15))
status_label.grid(row=0, column=0, columnspan=3, pady=5)

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                      command=lambda row=row, col=col: click(row, col))
        buttons[row][col].grid(row=row+1, column=col)

# Creating restart button
restart_button = tk.Button(root, text="Restart Game", font=('normal', 15), command=reset_game)

# To Run the application
root.mainloop()
