"""
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/


Given an array of integers nums, sort the array in ascending order.


-> Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

-> Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
1. 1 <= nums.length <= 5 * 10^4
2. -5 * 10^4 <= nums[i] <= 5 * 10^4
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sort array with a python func.

        Time Complexity: O(n * logn)
        Space Complexity: O(n)
        """
        return sorted(nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        """Selection sort.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        for i in range(len(nums) - 1):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        """Insertion sort.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        """Bubble sort.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        for i in range(len(nums)):
            for j in range(1, len(nums) - i):
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        """Merge sort.

        Time Complexity: O(n * logn)
        Space Complexity: O(n)
        """

        def merge(left: List[int], right: List[int]) -> List[int]:
            """Merge two list according to their values."""
            sorted_list = []

            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            sorted_list += left[i:]
            sorted_list += right[j:]
            return sorted_list

        if len(nums) <= 1:
            return nums

        mid_idx = len(nums) // 2
        left, right = nums[:mid_idx], nums[mid_idx:]
        left, right = self.sortArray(left), self.sortArray(right)
        return merge(left, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        """Quick sort.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]
        less, equal, more = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                equal.append(num)
        return self.sortArray(less) + self.sortArray(equal) + self.sortArray(more)
