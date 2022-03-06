"""
https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2901/


Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


-> Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

-> Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1. 1 <= heights.length <= 10^5
2. 0 <= heights[i] <= 10^4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Get the largest rectangle area."""
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            if not stack:
                stack.append([idx, height])
                continue

            prev_idx = idx
            while stack and height < stack[-1][1]:
                prev_idx, prev_height = stack.pop()
                max_area = max(prev_height * (idx - prev_idx), max_area)
            stack.append([prev_idx, height])

        # check the remains
        for idx, height in stack:
            max_area = max(height * (len(heights) - idx), max_area)
        return max_area
