"""
https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2903/


Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


-> Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

-> Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

-> Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1. 1 <= nums.length <= 6
2. -10 <= nums[i] <= 10
3. All the integers of nums are unique.
"""
from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Permutation."""
        outputs: List[List[int]] = []
        used: List[bool] = [False for _ in nums]

        def recursive(arr: List[int]) -> None:
            if len(arr) == len(nums):
                outputs.append(arr.copy())
                return

            for idx, num in enumerate(nums):
                if not used[idx]:
                    arr.append(num)
                    used[idx] = True
                    recursive(arr)
                    used[idx] = False
                    arr.pop()

        recursive([])
        return outputs
