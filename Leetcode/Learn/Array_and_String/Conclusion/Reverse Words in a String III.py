"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


-> Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

-> Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
1. 1 <= s.length <= 5 * 10^4
2. s contains printable ASCII characters.
3. s does not contain any leading or trailing spaces.
4. There is at least one word in s.
5. All the words in s are separated by a single space.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # Time: O(N)
        # Space: O(1)
        s = s.split()
        s = [word[::-1] for word in s]
        return " ".join(s)
