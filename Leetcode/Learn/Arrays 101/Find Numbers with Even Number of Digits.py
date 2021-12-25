"""
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/


Given an array nums of integers, return how many of them contain an even number of digits.


-> Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

-> Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Constraints:
1. 1 <= nums.length <= 500
2. 1 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """Find the number of num contains an even number of digits."""
        cnt = 0
        for num in nums:
            num_len = len(str(num))
            if num_len % 2 == 0:
                cnt += 1
        return cnt
