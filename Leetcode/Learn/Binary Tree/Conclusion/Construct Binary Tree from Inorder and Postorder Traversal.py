"""
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/


Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


-> Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

-> Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
1. 1 <= inorder.length <= 3000
2. postorder.length == inorder.length
3. -3000 <= inorder[i], postorder[i] <= 3000
4. inorder and postorder consist of unique values.
5. Each value of postorder also appears in inorder.
6. inorder is guaranteed to be the inorder traversal of the tree.
7. postorder is guaranteed to be the postorder traversal of the tree.
"""
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
    inorder, postorder = None, None

    def _buildTree(self, left: int, right: int) -> Optional[TreeNode]:
        """Build a Tree."""
        if left > right:
            return

        root = TreeNode(self.postorder.pop())
        idx = self.map_idx[root.val]

        # assign right
        root.right = self._buildTree(idx + 1, right)
        # assign left
        root.left = self._buildTree(left, idx - 1)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Build a Tree."""
        self.map_idx.update({val: idx for idx, val in enumerate(inorder)})
        self.inorder, self.postorder = inorder, postorder

        return self._buildTree(0, len(inorder) - 1)
