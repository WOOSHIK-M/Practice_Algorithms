"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/


Given a string s, find the length of the longest 
substring without repeating characters.

-> Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

-> Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

-> Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
1. 0 <= s.length <= 5 * 10^4
2. s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Window methods.

        Time: O(N)
        Space: O(N)
        """
        chars, answer = set(), 0

        l = 0
        for c in s:
            while c in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            answer = max(answer, len(chars))
        return answer