"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


-> Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

-> Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

-> Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1. 1 <= target <= 10^9
2. 1 <= nums.length <= 10^5
3. 1 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        answer = 1e5

        src, acc = 0, 0
        for des, val in enumerate(nums):
            acc += val
            while acc >= target:
                answer = min(des - src + 1, answer)
                acc -= nums[src]
                src += 1
        return answer if answer <= len(nums) else 0
