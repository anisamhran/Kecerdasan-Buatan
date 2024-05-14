import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, size=3, level='easy'):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.player = 'X'  # Set pemain sebagai X
        self.level = level
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.create_board()

    def create_board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Helvetica', 24), width=10, height=3, bg='light green', command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.buttons[row][col]['text'] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"{self.player} wins!")
                self.root.destroy()
            elif self.isfull():
                messagebox.showinfo("Tic Tac Toe", "Game draw!")
                self.root.destroy()
            else:
                if self.player == 'X':  # Hanya panggil langkah komputer jika pemain adalah X
                    self.player = 'O'
                    self.computer_move()

    def computer_move(self):
        if self.level == 'easy':
            row, col = self.get_random_move()
        else:
            row, col = self.get_best_move()
        self.board[row][col] = 'O'
        self.buttons[row][col]['text'] = 'O'
        if self.check_winner():
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            self.root.destroy()
        elif self.isfull():
            messagebox.showinfo("Tic Tac Toe", "Game draw!")
            self.root.destroy()
        else:
            self.player = 'X'  # Set giliran pemain kembali menjadi X setelah langkah bot

    def get_random_move(self):
        available_moves = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == ' ']
        return random.choice(available_moves)

    def get_best_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, False, -float('inf'), float('inf'))
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, board, maximizing, alpha, beta):
        if self.check_winner(board):
            return 1 if maximizing else -1
        elif self.isfull(board):
            return 0

        if maximizing:
            max_score = -float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, False, alpha, beta)
                        board[i][j] = ' '
                        max_score = max(max_score, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return max_score
        else:
            min_score = float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, True, alpha, beta)
                        board[i][j] = ' '
                        min_score = min(min_score, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return min_score

    def check_winner(self, board=None):
        if board is None:
            board = self.board

        for row in range(self.size):
            if board[row][0] == board[row][1] == board[row][2] != ' ':
                return True

        for col in range(self.size):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return True

        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True

        return False

    def isfull(self, board=None):
        if board is None:
            board = self.board

        return all(board[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def play(self):
        self.root.mainloop()

if __name__ == "__main__":
    size = int(input("Enter size of the board: "))
    level = input("Choose bot level (easy/hard): ")
    game = TicTacToeGUI(size, level)
    game.play()
