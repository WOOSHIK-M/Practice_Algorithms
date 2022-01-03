"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/


Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


-> Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

-> Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1. 1 <= nums.length <= 10^4
2. -10^4 <= nums[i] <= 10^4
3. nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Sort list according to component sq."""
        len_nums = len(nums)
        left, right = 0, len_nums - 1

        idx = len_nums - 1
        answer = [0 for _ in range(len_nums)]
        for _ in range(len_nums):
            left_val, right_val = nums[left], nums[right]
            if abs(left_val) > abs(right_val):
                answer[idx] = left_val * left_val
                left += 1
            else:
                answer[idx] = right_val * right_val
                right -= 1
            idx -= 1
        return answer

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Simple code."""
        return sorted([num * num for num in nums])
