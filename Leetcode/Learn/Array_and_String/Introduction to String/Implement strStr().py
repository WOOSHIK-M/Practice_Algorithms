# pylint: disable=too-few-public-methods
"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


-> Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

-> Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

-> Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
1. 0 <= haystack.length, needle.length <= 5 * 10^4
2. haystack and needle consist of only lower-case English characters.
"""
from typing import List


class Solution:
    """KMP algorithm: O(M+N)"""

    def computeLPSArray(self, pat: str, M: int, lps: List[int]) -> None:
        p_s_len = 0  # length of the previous longest prefix suffix

        lps[0] = 0  # lps[0] is always 0
        i = 1

        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i] == pat[p_s_len]:
                p_s_len += 1
                lps[i] = p_s_len
                i += 1
            else:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar
                # to search step.
                if p_s_len != 0:
                    p_s_len = lps[p_s_len - 1]

                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack:
            return -1

        M = len(needle)
        N = len(haystack)

        # create lps[] that will hold the longest prefix suffix
        # values for needle
        lps = [0] * M
        j = 0  # index for needle[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(needle, M, lps)

        i = 0  # index for haystack[]
        while i < N:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == M:
                return i - j

            # mismatch after j matches
            elif i < N and needle[j] != haystack[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
