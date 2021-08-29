"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


-> Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

-> Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1. 1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Time: O(numRows^2)
        # Space: O(numRows^2)
        answer: List[List[int]] = [[1]]
        
        if numRows == 1:
            return answer

        answer.append([1, 1])
        if numRows == 2:
            return answer

        for i in range(numRows - 2):
            tmp: List[int] = []
            for j in range(i + 1):
                tmp.append(answer[-1][j] + answer[-1][j + 1])
            tmp.insert(0, 1)
            tmp.append(1)
            answer.append(tmp)
    
        return answer
    
    def generate(self, numRows: int) -> List[List[int]]:
        # Time: O(numRows^2)
        # Space: O(numRows^2)
        res = [[1]]
        for _ in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
