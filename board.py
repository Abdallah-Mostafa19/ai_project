ROWS = 6
COLS = 7

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[0][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROWS - 1, -1, -1):
            if self.board[r][col] == 0:
                return r

    def winning_move(self, piece):
        # Horizontal
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(self.board[r][c + i] == piece for i in range(4)):
                    return True

        # Vertical
        for c in range(COLS):
            for r in range(ROWS - 3):
                if all(self.board[r + i][c] == piece for i in range(4)):
                    return True

        # Positive Diagonal
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(self.board[r + i][c + i] == piece for i in range(4)):
                    return True

        # Negative Diagonal
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(self.board[r - i][c + i] == piece for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.board[0][c] != 0 for c in range(COLS))
