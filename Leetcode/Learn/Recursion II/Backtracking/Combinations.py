"""
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2798/


Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.


-> Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

-> Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
1. 1 <= n <= 20
2. 1 <= k <= n
"""
from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Get combinations with itertools."""
        return list(combinations(range(1, n + 1), k))

    def combine(self, n: int, k: int) -> List[List[int]]:
        """Get combinations recursively."""
        if k == 0:
            return [[]]
        return [
            pre + [i] for i in range(k, n + 1) for pre in self.combine(i - 1, k - 1)
        ]

    def combine(self, n: int, k: int) -> List[List[int]]:
        """Get combinations with DFS."""

        result = []

        nums = range(1, n + 1)
        visited = [False for _ in range(n)]

        def dfs(arr: List[int]) -> None:
            """Implement DFS."""
            if len(arr) == k:
                result.append(arr.copy())
                return

            src = arr[-1] if arr else 0
            for nxt in range(src, len(nums)):
                if not visited[nxt]:
                    arr.append(nums[nxt])
                    visited[nxt] = True

                    dfs(arr)

                    arr.pop()
                    visited[nxt] = False

        dfs([])
        return result
