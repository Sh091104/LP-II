import matplotlib.pyplot as plt
import numpy as np

class NQueensBacktracking:
    def __init__(self, N):
        self.N = N
        self.board = [-1] * N
        self.solutions = []
        self.step_counter = 1
        self.group_counter = 1

    def print_board(self):
        board_copy = np.zeros((self.N, self.N), dtype=int)
        for row in range(self.N):
            if self.board[row] != -1:
                board_copy[row, self.board[row]] = 1
        return board_copy

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_nq_util(self, row):
        if row == self.N:
            self.solutions.append(self.board.copy())
            return True

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row] = col
                self.show_step()
                if self.solve_nq_util(row + 1):
                    return True
                self.board[row] = -1
        return False

    def show_step(self):
        board_state = self.print_board()
        plt.figure(figsize=(6, 6))
        plt.imshow(board_state, cmap='Blues', interpolation='none')
        plt.title(f"Step {self.step_counter} (Group {self.group_counter})")
        plt.xticks(range(self.N))
        plt.yticks(range(self.N))
        plt.grid(True)
        for i in range(self.N):
            for j in range(self.N):
                if board_state[i, j] == 1:
                    plt.text(j, i, "Q", color="red", fontsize=20, ha='center', va='center')
        plt.show()

        self.step_counter += 1
        if (self.step_counter - 1) % 3 == 0:
            self.group_counter += 1
            self.step_counter = 1

    def solve_nq(self):
        if not self.solve_nq_util(0):
            print("Solution does not exist")
            return
        print(f"Final solution for {self.N}-Queens Problem:")
        self.show_solution()

    def show_solution(self):
        final_board = self.print_board()
        plt.figure(figsize=(6, 6))
        plt.imshow(final_board, cmap='Blues', interpolation='none')
        plt.title(f"Final Solution")
        plt.xticks(range(self.N))
        plt.yticks(range(self.N))
        plt.grid(True)
        for i in range(self.N):
            for j in range(self.N):
                if final_board[i, j] == 1:
                    plt.text(j, i, "Q", color="red", fontsize=20, ha='center', va='center')
        plt.show()

# Take user input for N
try:
    N = int(input("Enter the value of N (size of the chessboard): "))
    if N < 1:
        print("Please enter a positive integer for N.")
    else:
        n_queens = NQueensBacktracking(N)
        n_queens.solve_nq()
except ValueError:
    print("Invalid input! Please enter an integer.")

"""
4
"""