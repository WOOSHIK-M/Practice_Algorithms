"""
https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


-> Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

-> Example 2:
Input: head = []
Output: []

-> Example 3:
Input: head = [1]
Output: [1]

Constraints:
1. The number of nodes in the list is in the range [0, 100].
2. 0 <= Node.val <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Swap every two adjacent nodes and return its head."""
        if not head or not head.next:
            return head

        nt_head = head.next
        head.next = self.swapPairs(nt_head.next)
        nt_head.next = head

        return nt_head


            