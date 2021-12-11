"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

-- figure --


-> Example 1:
Input: rowIndex = 3
Output: [1,3,3,1] 

-> Example 2:
Input: rowIndex = 0
Output: [1]

-> Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
1. 0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Time: O(rowIndex)
        # Space: O(rowIndex)
        answer = [0 for _ in range(rowIndex + 1)]
        answer[0] = 1

        for i in range(rowIndex + 1):
            for j in range(1, i + 1)[::-1]:
                answer[j] += answer[j - 1]
        return answer
