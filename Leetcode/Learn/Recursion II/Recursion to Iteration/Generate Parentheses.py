"""
https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2772/


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


-> Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

-> Exmaple 2:
Input: n = 1
Output: ["()"]

Constraints:
1. 1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Generate parenthesis."""
        parentheses = []

        def backtrack(
            parenthesis: List[str] = [], open: int = 0, close: int = 0
        ) -> None:
            """Backtracking."""
            if len(parenthesis) == 2 * n:
                parentheses.append("".join(parenthesis))
                return

            if open < n:
                parenthesis.append("(")
                backtrack(parenthesis, open + 1, close)
                parenthesis.pop()

            if close < open:
                parenthesis.append(")")
                backtrack(parenthesis, open, close + 1)
                parenthesis.pop()

        backtrack()
        return parentheses
