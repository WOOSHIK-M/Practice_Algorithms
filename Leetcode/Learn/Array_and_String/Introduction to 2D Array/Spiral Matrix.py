"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/

Given an m x n matrix, return all elements of the matrix in spiral order.


-> Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

-> Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1. m == matrix.length
2. n == matrix[i].length
3. 1 <= m, n <= 10
4. -100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(n*(m^2)+m(n^2) / 2)
        # Space: O(n*m)
        answer: List[int] = []

        while matrix:
            answer += matrix[0]
            del matrix[0]
            matrix = [row for row in zip(*matrix)][::-1]
        return answer
