"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/

Given an array, rotate the array to the right by k steps, where k is non-negative.


-> Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

-> Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1. 1 <= nums.length <= 10^5
2. -2^31 <= nums[i] <= 2^31 - 1
3. 0 <= k <= 10^5

Follow up:
1. Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
2. Could you do it in-place with O(1) extra space?
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time: O(1)
        Space: O(n)
        """
        nums = nums[-k:] + nums
        del nums[-k:]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Time: O(1)
        Space: O(n)
        """
        k = k % len(nums)
        if not k:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
