"""
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/


Given the head of a singly linked list, reverse the list, and return the reversed list.


-> Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

-> Example 2:
Input: head = [1,2]
Output: [2,1]

-> Example 3:
Input: head = []
Output: []

Constraints:
1. The number of nodes in the list is the range [0, 5000].
2. -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse List iteratively.

        Notes:
            1. 1 -> 2 -> 3 -> 4 -> 5
            2. 1 <- 2 -> 3 -> 4 -> 5
            3. ...
        """
        cur_node = parent = None
        while head:
            cur_node, head = head, head.next
            cur_node.next, parent = parent, cur_node
        return cur_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse List recursively.

        Notes:
            1. 1 -> 2 -> 3 -> 4 <- 5
            2. 1 -> 2 -> 3 <- 4 <- 5
            3. ...
        """
        if not head or not head.next:
            return head

        first_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return first_node
