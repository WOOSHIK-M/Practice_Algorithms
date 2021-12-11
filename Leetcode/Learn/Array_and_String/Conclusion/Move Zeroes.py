"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1174/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


-> Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

-> Example 2:
Input: nums = [0]
Output: [0]

Constraint:
1. 1 <= nums.length <= 10^4
2. -2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(N)
        # Space: O(1)
        left = 0
        for idx, num in enumerate(nums):
            if num == 0:
                continue

            nums[left], nums[idx] = num, nums[left]
            left += 1
