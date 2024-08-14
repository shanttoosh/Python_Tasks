import tkinter as tk

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER1 = 1
PLAYER2 = 2
EMPTY = 0
PLAYER1_COLOR = "red"
PLAYER2_COLOR = "yellow"

class ConnectFour:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")

        self.board = [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.current_player = PLAYER1

        self.canvas = tk.Canvas(self.master, width=700, height=600, bg="blue")
        self.canvas.pack()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game, font=("Helvetica", 14))
        self.restart_button.pack(pady=10)

        self.draw_board()

        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        """Draw the Connect Four board."""
        self.canvas.delete("all")
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                x_start = c * 100
                y_start = r * 100
                self.canvas.create_oval(
                    x_start + 10, y_start + 10, x_start + 90, y_start + 90,
                    fill="white", outline="black"
                )
        self.draw_pieces()

    def draw_pieces(self):
        """Draw the pieces on the board."""
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                x_start = c * 100
                y_start = (ROW_COUNT - r - 1) * 100
                if self.board[r][c] == PLAYER1:
                    color = PLAYER1_COLOR
                elif self.board[r][c] == PLAYER2:
                    color = PLAYER2_COLOR
                else:
                    continue
                self.canvas.create_oval(
                    x_start + 10, y_start + 10, x_start + 90, y_start + 90,
                    fill=color, outline="black"
                )

    def handle_click(self, event):
        """Handle mouse click events."""
        col = int(event.x // 100)
        if self.is_valid_location(col):
            row = self.get_next_open_row(col)
            self.drop_piece(row, col)

            if self.winning_move(self.current_player):
                self.draw_board()
                self.canvas.unbind("<Button-1>")  # Disable further moves
                winner = "Player 1" if self.current_player == PLAYER1 else "Player 2"
                self.show_winner(winner)
            else:
                self.current_player = PLAYER2 if self.current_player == PLAYER1 else PLAYER1

            self.draw_board()

            if self.is_board_full():
                self.canvas.unbind("<Button-1>")  # Disable further moves
                self.show_winner("No one")

    def drop_piece(self, row, col):
        """Place a piece on the board."""
        self.board[row][col] = self.current_player

    def is_valid_location(self, col):
        """Check if a column is valid for a move."""
        return self.board[ROW_COUNT - 1][col] == EMPTY

    def get_next_open_row(self, col):
        """Get the next open row in the specified column."""
        for row in range(ROW_COUNT):
            if self.board[row][col] == EMPTY:
                return row

    def winning_move(self, piece):
        """Check for a win condition."""
        for col in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT):
                if (self.board[row][col] == piece and
                    self.board[row][col + 1] == piece and
                    self.board[row][col + 2] == piece and
                    self.board[row][col + 3] == piece):
                    return True

        for col in range(COLUMN_COUNT):
            for row in range(ROW_COUNT - 3):
                if (self.board[row][col] == piece and
                    self.board[row + 1][col] == piece and
                    self.board[row + 2][col] == piece and
                    self.board[row + 3][col] == piece):
                    return True

        for col in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT - 3):
                if (self.board[row][col] == piece and
                    self.board[row + 1][col + 1] == piece and
                    self.board[row + 2][col + 2] == piece and
                    self.board[row + 3][col + 3] == piece):
                    return True

        for col in range(COLUMN_COUNT - 3):
            for row in range(3, ROW_COUNT):
                if (self.board[row][col] == piece and
                    self.board[row - 1][col + 1] == piece and
                    self.board[row - 2][col + 2] == piece and
                    self.board[row - 3][col + 3] == piece):
                    return True

        return False

    def is_board_full(self):
        """Check if the board is full."""
        return not any(self.is_valid_location(col) for col in range(COLUMN_COUNT))

    def show_winner(self, winner):
        """Display the winner."""
        winner_text = f"{winner} wins!" if winner != "No one" else "It's a draw!"
        winner_label = tk.Label(self.master, text=winner_text, font=("Helvetica", 24))
        winner_label.pack()

    def restart_game(self):
        """Restart the game."""
        self.board = [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.current_player = PLAYER1
        self.canvas.bind("<Button-1>", self.handle_click)  # Re-enable moves
        self.draw_board()
        for widget in self.master.pack_slaves():
            if isinstance(widget, tk.Label):
                widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
