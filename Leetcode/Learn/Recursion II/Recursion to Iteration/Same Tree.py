"""
https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2894/


Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


-> Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

-> Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

-> Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
1. The number of nodes in both trees is in the range [0, 100].
2. -10^4 <= Node.val <= 10^4
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check if they are the same."""
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
