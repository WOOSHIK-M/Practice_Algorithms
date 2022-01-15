"""
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/


The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.


-> Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

-> Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

-> Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
1. 0 <= n <= 30
"""


class Solution:
    def fib(self, n: int) -> int:
        """Calculate n-th Fibonacci number."""
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def fib(self, n: int) -> int:
        """Calculate n-th Fibonacci number with for-loop."""
        arr = [0, 1, 1]
        if n <= 2:
            return arr[n]

        for _ in range(3, n + 1):
            arr[2], arr[1] = arr[1] + arr[2], arr[2]
        return arr[2]
