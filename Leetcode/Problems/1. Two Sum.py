"""
https://leetcode.com/problems/two-sum/description/


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

-> Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

-> Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

-> Exmample 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
1. 2 <= nums.length <= 10^4
2. -10^9 <= nums[i] <= 10^9
3. -10^9 <= target <= 10^9
4. Only one valid answer exists.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Bruto-force method.
        
        Time: O(N^2)
        Space: O(1)
        """
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1 + 1:]):
                if num1 + num2 == target:
                    return [idx1, idx1 + idx2 + 1]
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Optimized time complexity.
        
        Time: O(N)
        Space: O(N)
        """
        d_num_index = dict()
        for idx, num in enumerate(nums):
            if target - num  in d_num_index:
                return [d_num_index[target - num], idx]
            d_num_index[num] = idx