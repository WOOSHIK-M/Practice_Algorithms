"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/


You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.


-> Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

-> Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

-> Example 3:
Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

Constraints:
1. 1 <= nums.length <= 50
2. 0 <= nums[i] <= 100
3. The largest element in nums is unique.
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        if len(nums) == 1: return 0
        
        max_num = max(nums)
        max_idx = nums.index(max_num)

        nums.remove(max_num)
        if max_num >= max(nums) * 2:
            return max_idx

        return -1
    
    def dominantIndex(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        if len(nums) == 1: return 0

        fir, sec, idx = -1, -1, 0
        for i, num in enumerate(nums):
            if num > fir:
                sec = fir
                fir = num
                idx = i
            elif num > sec:
                sec = num
        
        if fir < sec * 2:
            idx = -1

        return idx 
