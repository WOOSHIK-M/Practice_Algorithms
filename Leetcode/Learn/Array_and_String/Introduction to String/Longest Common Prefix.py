"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


-> Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

-> Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraint:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: O(strnum * strlen)
        # Space: O(strlen)
        answer: str = ""

        len_str: List[int] = [len(word) for word in strs]

        iter_num = min(len_str)
        for idx in range(iter_num):
            alphabet = strs[0][idx]

            for word_check in strs[1:]:
                if alphabet != word_check[idx]:
                    return answer
            answer += alphabet
        return answer

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: O(strnum * strlen)
        # Space: O(strlen)
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
