"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/

Given a binary array nums, return the maximum number of consecutive 1's in the array.


-> Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

-> Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1. 1 <= nums.length <= 10^5
2. nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        answer = 0

        idx, tmp_leng, leng = 0, 0, len(nums)
        while idx < leng:
            if nums[idx] == 1:
                tmp_leng += 1
                answer = max(tmp_leng, answer)
            else:
                tmp_leng = 0
            idx += 1
        return answer
