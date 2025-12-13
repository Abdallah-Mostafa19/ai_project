import tkinter as tk
from board import Board, ROWS, COLS
from minimax import minimax

CELL_SIZE = 80

class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4 - Human vs AI")

        self.board = Board()
        self.current_player = 1  # Human = 1, AI = 2

        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL_SIZE,
            height=(ROWS + 1) * CELL_SIZE,
            bg="blue"
        )
        self.canvas.pack()

        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        self.canvas.delete("all")
        for c in range(COLS):
            for r in range(ROWS):
                x1 = c * CELL_SIZE
                y1 = (r + 1) * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                piece = self.board.board[r][c]
                color = "white"
                if piece == 1:
                    color = "red"
                elif piece == 2:
                    color = "yellow"

                self.canvas.create_oval(
                    x1 + 5, y1 + 5,
                    x2 - 5, y2 - 5,
                    fill=color
                )

    def handle_click(self, event):
        # Human move
        col = event.x // CELL_SIZE
        if col < 0 or col >= COLS:
            return

        if self.board.is_valid_location(col):
            row = self.board.get_next_open_row(col)
            self.board.drop_piece(row, col, 1)  # Human
            self.draw_board()

            if self.board.winning_move(1):
                self.show_message("You Win!")
                return

            if self.board.is_full():
                self.show_message("Draw!")
                return

            # AI move
            ai_col = minimax(self.board, depth=4, alpha=-float('inf'), beta=float('inf'), maximizingPlayer=True)
            if ai_col is not None:
                ai_row = self.board.get_next_open_row(ai_col)
                self.board.drop_piece(ai_row, ai_col, 2)  # AI
                self.draw_board()

                if self.board.winning_move(2):
                    self.show_message("AI Wins!")
                elif self.board.is_full():
                    self.show_message("Draw!")

    def show_message(self, msg):
        popup = tk.Toplevel()
        popup.title("Game Over")
        tk.Label(popup, text=msg, font=("Arial", 18)).pack(padx=20, pady=20)
        tk.Button(popup, text="Restart", command=lambda: [popup.destroy(), self.restart_game()]).pack(pady=10)

    def restart_game(self):
        self.board = Board()
        self.current_player = 1
        self.draw_board()
