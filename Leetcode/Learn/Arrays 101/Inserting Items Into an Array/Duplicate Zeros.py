"""
https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/


Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


-> Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

-> Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
1. 1 <= arr.length <= 10^4
2. 0 <= arr[i] <= 9
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_arr, n_zeros = len(arr), arr.count(0)
        for idx in range(len_arr - 1, -1, -1):
            # put the value into the behind of array
            if idx + n_zeros < len_arr:
                arr[idx + n_zeros] = arr[idx]

            if arr[idx] == 0:
                n_zeros -= 1
                # duplicate zero
                if idx + n_zeros < len_arr:
                    arr[idx + n_zeros] = 0
