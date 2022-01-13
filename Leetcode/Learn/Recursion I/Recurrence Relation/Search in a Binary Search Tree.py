"""
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/


You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


-> Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

-> Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
1. The number of nodes in the tree is in the range [1, 5000].
2. 1 <= Node.val <= 10^7
3. root is a binary search tree.
4. 1 <= val <= 10^7
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """TreeNode class."""

    def __init__(self, val=0, left=None, right=None):
        """Initialize."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Search BST."""
        if root:
            if root.val == val:
                return root
            return (
                self.searchBST(root.left, val)
                if root.val > val
                else self.searchBST(root.right, val)
            )
