"""
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2872/


Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.


-> Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

-> Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:
1. m == matrix.length
2. n == matrix[i].length
3. 1 <= n, m <= 300
4. -10^9 <= matrix[i][j] <= 10^9
5. All the integers in each row are sorted in ascending order.
6. All the integers in each column are sorted in ascending order.
7. -10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Search matrix."""
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            val = matrix[row][col]

            if val == target:
                return True

            if val < target:
                row += 1
            elif val > target:
                col -= 1
        return False
