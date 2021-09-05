"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/

Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.


-> Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

-> Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

-> Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

Constraint:
1. 2 <= numbers.length <= 3 * 10^4
2. -1000 <= numbers[i] <= 1000
3. numbers is sorted in non-decreasing order.
4. -1000 <= target <= 1000
5. The tests are generated such that there is exactly one solution.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        num_dict = dict()
        for idx, num in enumerate(numbers):
            if target - num in num_dict.keys():
                return [num_dict[target - num] + 1, idx + 1]
            num_dict[num] = idx

    def twoSum(self, numbers, target):
        # Time: O(n)
        # Space: O(1)
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
