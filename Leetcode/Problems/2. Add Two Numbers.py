"""
https://leetcode.com/problems/add-two-numbers/


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

LeetCode Logo
Problem List
Premium
0

avatar
2. Add Two Numbers
Medium
24.6K
4.8K
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
1. The number of nodes in each linked list is in the range [1, 100].
2. 0 <= Node.val <= 9
3. It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Memory trick.
        
        Time: O(N)
        Space: O(N)
        """
        carry = 0
        ans = tmp = ListNode()

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            import pdb; pdb.set_trace()
            tmp.next = tmp = ListNode(val)
        return ans.next

l1 = ListNode(
    val=2,
    next=ListNode(
        val=4,
        next=ListNode(
            val=3,
            next=None,
        )
    )
)

l2 = ListNode(
    val=5,
    next=ListNode(
        val=6,
        next=ListNode(
            val=4,
            next=None,
        )
    )
)
sol = Solution()
ans = sol.addTwoNumbers(l1, l2)
print(ans)