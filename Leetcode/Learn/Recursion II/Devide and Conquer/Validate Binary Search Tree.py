"""
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2874/


Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.


-> Example 1:
Input: root = [2,1,3]
Output: true

-> Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
1. The number of nodes in the tree is in the range [1, 10^4].
2. -2^31 <= Node.val <= 2^31 - 1
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Validate binary search tree."""

        def _isValidBST(root: TreeNode, lower: int, upper: int) -> bool:
            if lower is not None and root.val <= lower:
                return False
            if upper is not None and root.val >= upper:
                return False

            is_valid = _isValidBST(root.left, lower, root.val) if root.left else True
            if is_valid:
                is_valid = (
                    _isValidBST(root.right, root.val, upper) if root.right else True
                )
            return is_valid

        if not root:
            return True
        return _isValidBST(root, None, None)
