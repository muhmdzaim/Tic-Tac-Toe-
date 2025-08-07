import tkinter as tk
from tkinter import messagebox

# Global variables to track the game state
current_player = "X"
board = [""] * 9 # Empty board with 9 positions
buttons = [] # List to store all button widgets
game_over = False

def create_window():
    """Create the main game window"""
    window = tk.Tk()
    window.title("Tic-Tac-Toe Game")
    window.geometry("600x600")
    window.configure(bg="light blue")
    window.resizable(False, False)
    return window

def check_winner():
    """Check if there's a winner or if the game is a tie"""
    global game_over

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            game_over = True
            messagebox.showinfo("Game Over", f"Player {board[combo[0]]} wins!")
            return True

    if "" not in board:
        game_over = True
        messagebox.showinfo("Game Over", "It's a tie!")
        return True
    
    return False

def button_click(position):
    """Handle button clicks"""
    global current_player

    if game_over or board[position] != "":
        return

    board[position] = current_player
    buttons[position].config(text=current_player, state="disabled")

    if not check_winner():
        current_player = "O" if current_player == "X" else "X"
        update_status_label()

def reset_game():
    """Reset the game to start over"""
    global current_player, board, game_over

    current_player = "X"
    board = [""] * 9
    game_over = False

    for button in buttons:
        button.config(text="", state="normal")

    update_status_label()

def update_status_label():
    """Update the status label to show current player"""
    status_label.config(text=f"Current Player: {current_player}")

def create_game_board(window):
    """Create the 3x3 grid of buttons"""
    
    global buttons

    board_frame = tk.Frame(window)
    board_frame.pack(pady=10)

    for i in range(9):
        row = i // 3
        col = i % 3
        button = tk.Button(
            board_frame,
            text="",
            width=6,
            height=3,
            font=("Comic Sans MS", 20, "bold"),
            command=lambda pos=i: button_click(pos)
        )
        button.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(button)

def create_controls(window):
    """Create the control buttons and status label"""
    global status_label

    status_label = tk.Label(
        window,
        text=f"Current Player: {current_player}",
        font=("Arial", 12),bg=("light blue")
    )
    status_label.pack(pady=5)

    reset_button = tk.Button(
        window,
        text="New Game",
        font=("Arial", 12),
        command=reset_game
    )
    reset_button.pack(pady=5)

def main():
    """Main function to start the game"""
    window = create_window()

    title_label = tk.Label(
        window,
        text="Tic-Tac-Toe",
        font=("Arial", 16, "bold")
    )
    title_label.pack(pady=10)

    create_game_board(window)
    create_controls(window)

    window.mainloop()

if __name__ == "__main__":
    main()