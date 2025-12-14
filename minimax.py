from board import ROWS, COLS
import copy

AI_PIECE = 2
HUMAN_PIECE = 1

def score_position(board, piece):
    score = 0

    # Horizontal
    for r in range(ROWS):
        row_array = board.board[r]
        for c in range(COLS - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Vertical
    for c in range(COLS):
        col_array = [board.board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Positive Diagonal
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board.board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Negative Diagonal
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            window = [board.board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def evaluate_window(window, piece):
    score = 0
    opp_piece = HUMAN_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4  # Block opponent

    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = [c for c in range(COLS) if board.is_valid_location(c)]

    is_terminal = board.winning_move(AI_PIECE) or board.winning_move(HUMAN_PIECE) or board.is_full()
    if depth == 0 or is_terminal:
        return None if len(valid_locations) == 0 else valid_locations[0]

    if maximizingPlayer:
        value = -float('inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            b_copy = copy.deepcopy(board)
            row = b_copy.get_next_open_row(col)
            b_copy.drop_piece(row, col, AI_PIECE)
            score = score_position(b_copy, AI_PIECE)
            if score > value:
                value = score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cut-off
        return best_col
    else:
        value = float('inf')
        best_col = valid_locations[0]
        for col in valid_locations:
            b_copy = copy.deepcopy(board)
            row = b_copy.get_next_open_row(col)
            b_copy.drop_piece(row, col, HUMAN_PIECE)
            score = score_position(b_copy, HUMAN_PIECE)
            if score < value:
                value = score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break  # Alpha cut-off
        return best_col
