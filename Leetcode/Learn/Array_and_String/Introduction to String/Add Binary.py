"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/

Given two binary strings a and b, return their sum as a binary string.


-> Example 1:
Input: a = "11", b = "1"
Output: "100"

-> Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1. 1 <= a.length, b.length <= 104
2. a and b consist only of '0' or '1' characters.
3. Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time: O(|a|+|b|)
        # Space: O(|a|+|b|)
        answer = ""

        a, b = list(a), list(b)
        r = 0
        
        while a or b or r:
            n = r
            if a:
                n += int(a.pop())
            if b:
                n += int(b.pop())

            answer += str(n % 2)
            r = n // 2
        return answer[::-1]
