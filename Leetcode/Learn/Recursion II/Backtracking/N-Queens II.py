"""
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2804/


The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.


-> Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

-> Example 2:
Input: n = 1
Output: 1

Constraints:
1. 1 <= n <= 9
"""
from typing import List


class Solution:

    n_validations = 0

    def totalNQueens(self, n: int) -> int:
        """Total n queens."""
        arr = [0 for _ in range(n)]
        self._place_a_queen(arr, 0, n)
        return self.n_validations

    def _place_a_queen(self, arr: List[int], row: int, n: int) -> None:
        """Count the vaild placements."""
        if row == n:
            self.n_validations += 1
            return

        for i in range(n):
            arr[row] = i
            if self._check_vaildation(arr, row):
                self._place_a_queen(arr, row + 1, n)

    def _check_vaildation(self, arr: List[int], row: int) -> None:
        """Make sure the current line has a valid location."""
        for i in range(row):
            if arr[i] == arr[row] or row - i == abs(arr[i] - arr[row]):
                return False
        return True
