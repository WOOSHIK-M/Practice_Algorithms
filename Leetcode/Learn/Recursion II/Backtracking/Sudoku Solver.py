"""
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2796/


Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.


-> Example 1:
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
1. board.length == 9
2. board[i].length == 9
3. board[i][j] is a digit or '.'.
4. It is guaranteed that the input board has only one solution.
"""
from typing import List


class Solution:

    GRID_SIZE = 9
    SUB_GRID_SIZE = 3

    candidates: List[str] = [str(i) for i in range(1, 10)]

    def is_valid(self, board, candidate: int, row: int, col: int) -> bool:
        """Check if it is the valid candidate."""

        def get_range(idx) -> range:
            """Get the range with the given row and col."""
            idx -= idx % self.SUB_GRID_SIZE
            return range(idx, idx + self.SUB_GRID_SIZE)

        row_check = all(board[i][col] != candidate for i in range(self.GRID_SIZE))
        col_check = all(board[row][i] != candidate for i in range(self.GRID_SIZE))
        grid_check = all(
            board[i][j] != candidate for i in get_range(row) for j in get_range(col)
        )
        return row_check and col_check and grid_check

    def dfs(self, board, row, col):
        """Implement DFS."""
        # solved
        if row == self.GRID_SIZE - 1 and col == self.GRID_SIZE:
            return True

        # next row
        if col == self.GRID_SIZE:
            row += 1
            col = 0

        if board[row][col] != ".":
            return self.dfs(board, row, col + 1)

        for candidate in self.candidates:
            if self.is_valid(board, candidate, row, col):
                board[row][col] = candidate
                if self.dfs(board, row, col + 1):
                    return True
            board[row][col] = "."
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0, 0)
