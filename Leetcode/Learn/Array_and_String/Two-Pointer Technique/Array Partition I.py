"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/

Given an integer array nums of 2n integers, group these integers into n pairs (a_1, b_1), (a_2, b_2), ..., (a_n, b_n) such that the sum of min(a_i, b_i) for all i is maximized. Return the maximized sum.


-> Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.

-> Example 2:
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
 
Constraint:
1 <= n <= 10^4
nums.length == 2 * n
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[2 * i] for i in range(len(nums) // 2))