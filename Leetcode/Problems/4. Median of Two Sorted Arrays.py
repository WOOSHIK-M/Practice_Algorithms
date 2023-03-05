"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/


Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

-> Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

-> Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
1. nums1.length == m
2. nums2.length == n
3. 0 <= m <= 1000
4. 0 <= n <= 1000
5. 1 <= m + n <= 2000
7. -10^6 <= nums1[i], nums2[i] <= 10^6
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Use sorted python function.
        
        Time: O((m+n) * log(m+n))
        Space: O(1)
        """
        nums = sorted(nums1 + nums2)
        n_nums = len(nums)
        if n_nums % 2:
            return nums[n_nums // 2]
        else:
            median = n_nums // 2
            return (nums[median - 1] + nums[median]) / 2
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Make a new list.

        Time: O(max(m,n))
        Space: O(m+n)
        """
        nums = [0 for _ in range(len(nums1) + len(nums2))]
        
        i = j = k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        
        while i < len(nums1):
            nums[k] = nums1[i]
            i += 1
            k += 1
        
        while j < len(nums2):
            nums[k] = nums2[j]
            j += 1
            k += 1
        
        median = len(nums) // 2
        if len(nums) % 2:
            return nums[median]
        else:
            return (nums[median - 1] + nums[median]) / 2
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Use binary search to two lists.
        
        Time: O(log(min(m,n)))
        Space: O(1)


        Methods:
            nums1: [..., x1, x2, ...]
                    |--- i ----|
            nums2: [..., ..., y1, y2, ...]
                    |------ j ------|
            i + j = index of median of two lists

            while match(x1, y1, x2, y2):
                if (x1, x2, y1, y2):
                    expand i
                elif (y1, y2, x1, x2):
                    expand j
            return (max(x1, y1) + min(x2, y2)) / 2
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        start, end, half_len = 0, m, (m + n + 1) // 2
        while start <= end:
            i = (start + end) // 2
            j = half_len - i

            x1 = float("-inf") if i == 0 else nums1[i - 1]
            x2 = float("inf") if i == m else nums1[i]
            y1 = float("-inf") if j == 0 else nums2[j - 1]
            y2 = float("inf") if j == n else nums2[j]

            if x1 <= y2 and y1 <= x2:
                if (m + n) % 2:
                    return max(x1, y1)
                else:
                    return ((max(x1, y1) + min(x2, y2)) / 2)
            elif y1 > x2:
                start = i + 1
            else:
                end = i - 1