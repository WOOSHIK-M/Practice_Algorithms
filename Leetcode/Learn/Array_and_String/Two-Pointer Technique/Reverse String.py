"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/

Write a function that reverses a string. The input string is given as an array of characters s.


-> Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

-> Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraint:
1 <= s.length <= 105
s[i] is a printable ascii character.

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = tmp

    def reverseString(self, s: List[str]) -> None:
        # bitwise inversion
        for i in range(len(s) // 2): s[i], s[~i] = s[~i], s[i]

sol = Solution().reverseString(["h","e","l","l","o"])