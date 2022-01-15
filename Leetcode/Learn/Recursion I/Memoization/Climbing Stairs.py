"""
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/


You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


-> Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

-> Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1. 1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """Climb stairs."""
        arr = [1, 1, 2]
        if n <= 2:
            return arr[n]

        for _ in range(3, n + 1):
            arr[1], arr[2] = arr[2], arr[1] + arr[2]
        return arr[2]
