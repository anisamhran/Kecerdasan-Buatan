# import numpy as np
# import tkinter as tk
# from tkinter import messagebox
# import pygame
# import sys
# import random

# ROW_COUNT = 6
# COLUMN_COUNT = 7
# EMPTY = 0
# PLAYER_1_PIECE = 1
# PLAYER_2_PIECE = 2
# SQUARESIZE = 75  # Perkecil ukuran kotak
# RADIUS = int(SQUARESIZE / 2 - 5)
# WIDTH = COLUMN_COUNT * SQUARESIZE
# HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
# SIZE = (WIDTH, HEIGHT)
# BLUE = (0, 0, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)

# def create_board():
#     return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

# def drop_piece(board, row, col, piece):
#     board[row][col] = piece

# def is_valid_location(board, col):
#     return board[ROW_COUNT - 1][col] == EMPTY

# def get_next_open_row(board, col):
#     for r in range(ROW_COUNT):
#         if board[r][col] == EMPTY:
#             return r

# def winning_move(board, piece):
#     # Check horizontal
#     for c in range(COLUMN_COUNT - 3):
#         for r in range(ROW_COUNT):
#             if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
#                 return True

#     # Check vertical
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT - 3):
#             if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
#                 return True

#     # Check positively sloped diagonals
#     for c in range(COLUMN_COUNT - 3):
#         for r in range(ROW_COUNT - 3):
#             if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
#                 return True

#     # Check negatively sloped diagonals
#     for c in range(COLUMN_COUNT - 3):
#         for r in range(3, ROW_COUNT):
#             if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
#                 return True

# def draw_board(board, screen):
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT):
#             pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
#             pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT):
#             if board[r][c] == PLAYER_1_PIECE:
#                 pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
#             elif board[r][c] == PLAYER_2_PIECE:
#                 pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
#     pygame.display.update()

# def evaluate_window(window, piece):
#     score = 0
#     opponent_piece = PLAYER_1_PIECE if piece == PLAYER_2_PIECE else PLAYER_2_PIECE

#     if window.count(piece) == 4:
#         score += 100
#     elif window.count(piece) == 3 and window.count(EMPTY) == 1:
#         score += 5
#     elif window.count(piece) == 2 and window.count(EMPTY) == 2:
#         score += 2

#     if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
#         score -= 4

#     return score

# def score_position(board, piece):
#     score = 0

#     # Score center column
#     center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
#     center_count = center_array.count(piece)
#     score += center_count * 3

#     # Score Horizontal
#     for r in range(ROW_COUNT):
#         row_array = [int(i) for i in list(board[r,:])]
#         for c in range(COLUMN_COUNT-3):
#             window = row_array[c:c+4]
#             score += evaluate_window(window, piece)

#     # Score Vertical
#     for c in range(COLUMN_COUNT):
#         col_array = [int(i) for i in list(board[:,c])]
#         for r in range(ROW_COUNT-3):
#             window = col_array[r:r+4]
#             score += evaluate_window(window, piece)

#     # Score positive sloped diagonal
#     for r in range(ROW_COUNT-3):
#         for c in range(COLUMN_COUNT-3):
#             window = [board[r+i][c+i] for i in range(4)]
#             score += evaluate_window(window, piece)

#     # Score negative sloped diagonal
#     for r in range(ROW_COUNT-3):
#         for c in range(COLUMN_COUNT-3):
#             window = [board[r+3-i][c+i] for i in range(4)]
#             score += evaluate_window(window, piece)

#     return score

# def is_terminal_node(board):
#     return winning_move(board, PLAYER_1_PIECE) or winning_move(board, PLAYER_2_PIECE) or len(get_valid_locations(board)) == 0

# def minimax(board, depth, maximizingPlayer):
#     valid_locations = get_valid_locations(board)
#     is_terminal = is_terminal_node(board)
#     if depth == 0 or is_terminal:
#         if is_terminal:
#             if winning_move(board, PLAYER_2_PIECE):
#                 return (None, 100000000000000)
#             elif winning_move(board, PLAYER_1_PIECE):
#                 return (None, -10000000000000)
#             else: # Game is over, no more valid moves
#                 return (None, 0)
#         else: # Depth is zero
#             return (None, score_position(board, PLAYER_2_PIECE))
#     if maximizingPlayer:
#         value = -np.Inf
#         column = random.choice(valid_locations)
#         for col in valid_locations:
#             row = get_next_open_row(board, col)
#             b_copy = board.copy()
#             drop_piece(b_copy, row, col, PLAYER_2_PIECE)
#             new_score = minimax(b_copy, depth-1, False)[1]
#             if new_score > value:
#                 value = new_score
#                 column = col
#         return column, value
#     else: # Minimizing player
#         value = np.Inf
#         column = random.choice(valid_locations)
#         for col in valid_locations:
#             row = get_next_open_row(board, col)
#             b_copy = board.copy()
#             drop_piece(b_copy, row, col, PLAYER_1_PIECE)
#             new_score = minimax(b_copy, depth-1, True)[1]
#             if new_score < value:
#                 value = new_score
#                 column = col
#         return column, value

# def get_valid_locations(board):
#     valid_locations = []
#     for col in range(COLUMN_COUNT):
#         if is_valid_location(board, col):
#             valid_locations.append(col)
#     return valid_locations

# def main():
#     board = create_board()
#     pygame.init()
#     screen = pygame.display.set_mode(SIZE)
#     draw_board(board, screen)
#     pygame.display.update()

#     turn = random.randint(PLAYER_1_PIECE, PLAYER_2_PIECE)  # Acak giliran pemain

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.MOUSEMOTION:
#                 pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
#                 posx = event.pos[0]
#                 if turn == PLAYER_1_PIECE:
#                     pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
#                 else:
#                     pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
#             pygame.display.update()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
#                 # Player 1 input
#                 if turn == PLAYER_1_PIECE:
#                     posx = event.pos[0]
#                     col = int(posx / SQUARESIZE)
#                     if is_valid_location(board, col):
#                         row = get_next_open_row(board, col)
#                         drop_piece(board, row, col, PLAYER_1_PIECE)
#                         if winning_move(board, PLAYER_1_PIECE):
#                             messagebox.showinfo("Result", "Player 1 wins!")
#                             sys.exit()
#                         turn = PLAYER_2_PIECE
#                 # Player 2 input (AI)
#                 else:
#                     col, minimax_score = minimax(board, 3, True)  # Kurangi kedalaman pencarian
#                     if is_valid_location(board, col):
#                         row = get_next_open_row(board, col)
#                         drop_piece(board, row, col, PLAYER_2_PIECE)
#                         if winning_move(board, PLAYER_2_PIECE):
#                             messagebox.showinfo("Result", "Player 2 wins!")
#                             sys.exit()
#                         turn = PLAYER_1_PIECE
#                 draw_board(board, screen)

# if __name__ == "__main__":
#     main()

import numpy as np
import tkinter as tk
from tkinter import messagebox
import pygame
import sys
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = 0
PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2
SQUARESIZE = 75  # Perkecil ukuran kotak
RADIUS = int(SQUARESIZE / 2 - 5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r

def winning_move(board, piece):
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True, ((r, c), (r, c+1), (r, c+2), (r, c+3))

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True, ((r, c), (r+1, c), (r+2, c), (r+3, c))

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True, ((r, c), (r+1, c+1), (r+2, c+2), (r+3, c+3))

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True, ((r, c), (r-1, c+1), (r-2, c+2), (r-3, c+3))

    return False, None

def draw_winning_line(screen, coords):
    for coord in coords:
        pygame.draw.circle(screen, (0, 255, 0), (int(coord[1] * SQUARESIZE + SQUARESIZE / 2), int(coord[0] * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS + 5)

def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_1_PIECE:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == PLAYER_2_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

def evaluate_window(window, piece):
    score = 0
    opponent_piece = PLAYER_1_PIECE if piece == PLAYER_2_PIECE else PLAYER_2_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Score positive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return winning_move(board, PLAYER_1_PIECE)[0] or winning_move(board, PLAYER_2_PIECE)[0] or len(get_valid_locations(board)) == 0

def minimax(board, depth, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, PLAYER_2_PIECE)[0]:
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_1_PIECE)[0]:
                return (None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, PLAYER_2_PIECE))
    if maximizingPlayer:
        value = -np.Inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_2_PIECE)
            new_score = minimax(b_copy, depth-1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else: # Minimizing player
        value = np.Inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_1_PIECE)
            new_score = minimax(b_copy, depth-1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def main():
    board = create_board()
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    draw_board(board, screen)
    pygame.display.update()

    turn = random.randint(PLAYER_1_PIECE, PLAYER_2_PIECE)  # Acak giliran pemain

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER_1_PIECE:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                # Player 1 input
                if turn == PLAYER_1_PIECE:
                    posx = event.pos[0]
                    col = int(posx / SQUARESIZE)
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_1_PIECE)
                        if winning_move(board, PLAYER_1_PIECE)[0]:
                            draw_winning_line(screen, winning_move(board, PLAYER_1_PIECE)[1])
                            draw_board(board, screen)  # Perbarui tampilan
                            messagebox.showinfo("Result", "Player 1 wins!")
                            sys.exit()
                    turn = PLAYER_2_PIECE
                # Player 2 input (AI)
                else:
                    col, minimax_score = minimax(board, 3, True)  # Kurangi kedalaman pencarian
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_2_PIECE)
                        if winning_move(board, PLAYER_2_PIECE)[0]:
                            draw_winning_line(screen, winning_move(board, PLAYER_2_PIECE)[1])
                            draw_board(board, screen)  # Perbarui tampilan
                            messagebox.showinfo("Result", "Player 2 wins!")
                            sys.exit()
                        turn = PLAYER_1_PIECE
                    draw_board(board, screen)  # Perbarui tampilan
                    
                    
if __name__ == "__main__":
    main()
