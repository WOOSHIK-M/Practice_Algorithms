"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/


Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


-> Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

-> Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

-> Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:
1. 1 <= nums.length <= 10^4
2. -2^31 <= nums[i] <= 2^31 - 1

Follow up: Can you find an O(n) solution?
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Find the third distinct maximum number."""
        num_0 = num_1 = num_2 = -float("inf")
        for num in nums:
            if num in (num_0, num_1, num_2):
                continue

            if num > num_0:
                num, num_0 = num_0, num
            if num > num_1:
                num, num_1 = num_1, num
            if num > num_2:
                num_2 = num
        return num_0 if num_2 == -float("inf") else num_2
