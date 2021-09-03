"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


-> Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

->Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraint:
1. m == mat.length
2. n == mat[i].length
3. 1 <= m, n <= 104
4. 1 <= m * n <= 104
5. -105 <= mat[i][j] <= 105
"""
from collections import defaultdict
from itertools import chain
from typing import Dict, List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Time: O(m*n)
        # Space: O(m*n)
        answer: List[int] = []

        sum_table: Dict[int, List[int]] = defaultdict(list)

        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(n):
                sum_table[row + col].append(mat[row][col])

        for k, v_s in sum_table.items():
            if k % 2 == 0:
                [answer.append(v) for v in v_s[::-1]]
            else:
                [answer.append(v) for v in v_s]

        return answer

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Time: O(m*n)
        # Space: O(m*n)
        d = defaultdict(list)
        for i, r in enumerate(mat):
            for j, c in enumerate(r):
                d[i + j] += (c,)

        return chain.from_iterable(v if k % 2 else v[::-1] for k, v in d.items())
