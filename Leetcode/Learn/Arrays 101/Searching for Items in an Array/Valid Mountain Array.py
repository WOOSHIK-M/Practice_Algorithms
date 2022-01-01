"""
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/


Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

* arr.length >= 3
* There exists some i with 0 < i < arr.length - 1 such that:
    * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


-> Example 1:
Input: arr = [2,1]
Output: false

-> Example 2:
Input: arr = [3,5,5]
Output: false

-> Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1. 1 <= arr.length <= 10^4
2. 0 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Verify the given array is a valid mountain array."""
        left, right, len_arr = 0, len(arr) - 1, len(arr)
        while left < len_arr - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right > 1 and arr[right] < arr[right - 1]:
            right -= 1
        return 0 < left == right < len_arr - 1
