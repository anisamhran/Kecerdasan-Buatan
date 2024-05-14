# import random
# # menghasilkan nilai acak
# # untuk memilih pemain pertama secara acak
# # menggunakan fungsi random.choice() untuk memilih secara acak dari daftar 

# # Fungsi untuk mencetak papan permainan
# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         # Menambahkan garis pada bawah tiap kolom
#         print("-" * 2 + "+" + "-" * 3 + "+" + "-" * 2)

# # Fungsi untuk memeriksa apakah ada pemenang
# # board[row][col] = current_player didefinisikan di funsi main
# # print_board(board) didefinisikan di funsi main
# def check_winner(board):
#     # Cek baris untuk mendapatkan pemenang
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] != " ":
#             return board[i][0]
#         # board[row][col] = current_player
#         # print_board(board)
#     # Cek kolom untuk mendapatkan pemenang  
#         if board[0][i] == board[1][i] == board[2][i] != " ":
#             return board[0][i]
#     # Cek diagonal untuk mendapatkan pemenang
#     if board[0][0] == board[1][1] == board[2][2] != " ":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != " ":
#         return board[0][2]
#     return None

# # Fungsi untuk mendapatkan sel-sel kosong di papan
# def get_empty_cells(board):
#     empty_cells = []
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == " ":
#                 empty_cells.append((i, j))
#     return empty_cells

# # Fungsi untuk memulai permainan Tic Tac Toe
# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     # Loop pertama for _ in range(3) digunakan untuk membuat baris-baris pada papan permainan. 
#     # Loop kedua for _ in range(3) digunakan untuk mengisi setiap elemen dalam setiap baris. 
#     # Setiap iterasi dari loop kedua akan mengisi satu elemen dalam baris tersebut dengan spasi kosong (" ").
#     players = ["X", "O"]
#     current_player = random.choice(players)
#     # penerapan import random
#     print("Selamat datang di permainan Tic Tac Toe!")
#     print("Papan Permainan:")
#     print_board(board)
#     # pemanggilan funsi print_board

#     while True:
# # loop yg terus berjalan selama kondisinya True
# # menjalankan seluruh langkah permainan sampai ada pemenang / permainan seri
#         print(f"Giliran pemain {current_player}")
#         while True:
#     # loop yang akan terus berjalan sampai input valid
#             try:
#                 row, col = map(int, input("Pilih baris dan kolom (1-3 dipisahkan dengan spasi): ").split())
#                 if 1 <= row <= 3 and 1 <= col <= 3:
#                     break
#                 else:
#                     print("Input tidak valid. Silakan masukkan angka dari 1 hingga 3.")
#             except ValueError:
#                 print("Input tidak valid. Silakan masukkan angka dari 1 hingga 3.")

#         row -= 1 # Mengubah input dari 1-3 menjadi 0-2 agar sesuai index array
#         col -= 1 # Mengubah input dari 1-3 menjadi 0-2 agar sesuai index array

#         if board[row][col] != " ":
#             print("Posisi sudah diisi. Silakan pilih lagi.")
#             continue

#         board[row][col] = current_player
#         print_board(board)

#         winner = check_winner(board)
#         if winner:
#             print(f"Pemain {winner} menang!")
#             break

#         if len(get_empty_cells(board)) == 0:
#             print("Permainan seri!")
#             break
#         current_player = "X" if current_player == "O" else "O"

# if __name__ == "__main__":
#     play_game()


# import random

# # Fungsi untuk mencetak papan permainan
# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         # Menambahkan garis pada bawah tiap kolom
#         print("-" * 2 + "+" + "-" * 3 + "+" + "-" * 2)

# # Fungsi untuk memeriksa apakah ada pemenang
# def check_winner(board):
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] != " ":
#             return board[i][0]
#         if board[0][i] == board[1][i] == board[2][i] != " ":
#             return board[0][i]
#     if board[0][0] == board[1][1] == board[2][2] != " ":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != " ":
#         return board[0][2]
#     return None

# # Fungsi untuk mendapatkan sel-sel kosong di papan
# def get_empty_cells(board):
#     empty_cells = []
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == " ":
#                 empty_cells.append((i, j))
#     return empty_cells

# # Fungsi untuk memilih langkah komputer secara acak dari sel-sel kosong yang tersedia
# def computer_move(board):
#     empty_cells = get_empty_cells(board)
#     return random.choice(empty_cells)

# # Fungsi untuk memulai permainan Tic Tac Toe
# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     players = ["X", "O"]
#     current_player = random.choice(players)
#     print("Selamat datang di permainan Tic Tac Toe!")
#     print("Papan Permainan:")
#     print_board(board)

#     while True:
#         if current_player == "X":
#             print(f"Giliran pemain {current_player}")
#             while True:
#                 try:
#                     row, col = map(int, input("Pilih baris dan kolom (1-3 dipisahkan dengan spasi): ").split())
#                     if 1 <= row <= 3 and 1 <= col <= 3:
#                         row -= 1
#                         col -= 1
#                         if board[row][col] != " ":
#                             print("Posisi sudah diisi. Silakan pilih lagi.")
#                             continue
#                         break
#                     else:
#                         print("Input tidak valid. Silakan masukkan angka dari 1 hingga 3.")
#                 except ValueError:
#                     print("Input tidak valid. Silakan masukkan angka dari 1 hingga 3.")
#             board[row][col] = current_player
#         else:
#             print(f"Giliran komputer {current_player}")
#             row, col = computer_move(board)
#             board[row][col] = current_player

#         print_board(board)

#         winner = check_winner(board)
#         if winner:
#             print(f"Pemain {winner} menang!")
#             break

#         if len(get_empty_cells(board)) == 0:
#             print("Permainan seri!")
#             break
#         current_player = "X" if current_player == "O" else "O"

# if __name__ == "__main__":
#     play_game()


import math

# Fungsi untuk mencetak papan permainan
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 2 + "+" + "-" * 3 + "+" + "-" * 2)

# Fungsi untuk memeriksa apakah ada pemenang
def check_winner(board):
    # Cek baris untuk mendapatkan pemenang
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    # Cek kolom untuk mendapatkan pemenang  
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Cek diagonal untuk mendapatkan pemenang
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Fungsi untuk mendapatkan sel-sel kosong di papan
def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

# Fungsi untuk mengevaluasi keuntungan langkah
def evaluate(board):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0

# Fungsi untuk melakukan langkah berdasarkan algoritma minimax
def minimax(board, depth, maximizing_player):
    if check_winner(board):
        return evaluate(board)
    
    if depth == 0 or len(get_empty_cells(board)) == 0:
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            eval = minimax(board, depth - 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            eval = minimax(board, depth - 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
        return min_eval


# Fungsi untuk memulai permainan Tic Tac Toe dengan algoritma minimax
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Selamat datang di permainan Tic Tac Toe!")
    print("Papan Permainan:")
    print_board(board)

    while True:
        player_move = input("Pilih baris dan kolom (1-3 dipisahkan dengan spasi): ")
        try:
            row, col = map(int, player_move.split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
                board[row - 1][col - 1] = "X"
                print_board(board)

                if check_winner(board):
                    print("Anda menang!")
                    break
                elif len(get_empty_cells(board)) == 0:
                    print("Permainan seri!")
                    break

                # Langkah AI
                best_eval = -math.inf
                best_move = None
                for row, col in get_empty_cells(board):
                    board[row][col] = "O"
                    eval = minimax(board, 16, False)
                    board[row][col] = " "
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (row, col)
                board[best_move[0]][best_move[1]] = "O"
                print("Giliran AI:")
                print_board(board)

                if check_winner(board):
                    print("AI menang!")
                    break
                elif len(get_empty_cells(board)) == 0:
                    print("Permainan seri!")
                    break
            else:
                print("Input tidak valid atau posisi sudah diisi. Silakan pilih lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka dari 1 hingga 3.")

if __name__ == "__main__":
    play_game()
