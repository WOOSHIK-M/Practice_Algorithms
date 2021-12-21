"""
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/


Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


-> Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

-> Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1. 1 <= preorder.length <= 3000
2. inorder.length == preorder.length
3. -3000 <= preorder[i], inorder[i] <= 3000
4. preorder and inorder consist of unique values.
5. Each value of inorder also appears in preorder.
6. preorder is guaranteed to be the preorder traversal of the tree.
7. inorder is guaranteed to be the inorder traversal of the tree.
"""
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    """TreeNode class."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        """Initialize."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    map_idx = dict()
    preorder: deque = deque()
    inorder: List[int] = []

    def _buildTree(self, left: int, right: int) -> Optional[TreeNode]:
        """Protected method for building a Tree."""
        if left > right:
            return

        root = TreeNode(self.preorder.popleft())
        idx = self.map_idx[root.val]

        # assign left
        root.left = self._buildTree(left, idx - 1)
        # assign right
        root.right = self._buildTree(idx + 1, right)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Build a Tree."""
        self.map_idx.update({val: idx for idx, val in enumerate(inorder)})
        self.preorder, self.inorder = deque(preorder), inorder

        return self._buildTree(0, len(self.preorder) - 1)
