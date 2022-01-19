"""
https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


-> Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

-> Example 2:
Input: list1 = [], list2 = []
Output: []

-> Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
1. The number of nodes in both lists is in the range [0, 50].
2. -100 <= Node.val <= 100
3. Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two lists recursively."""
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two lists iteratively."""
        head = tmp = ListNode(val=0)
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        tmp.next = list1 or list2
        return head.next
