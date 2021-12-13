"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


-> Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

-> Example 2:
Input: root = [1,null,2]
Output: 2

-> Example 3:
Input: root = []
Output: 0

-> Exmaple 4:
Input: root = [0]
Output: 1

Constraints:
1. The number of nodes in the tree is in the range [0, 10^4].
2. -100 <= Node.val <= 100
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
    max_depth = 0

    def dfs(self, root: Optional[TreeNode], cur_depth: int) -> None:
        """Implement dfs."""
        if root:
            cur_depth += 1
            self.dfs(root.left, cur_depth)
            self.dfs(root.right, cur_depth)
        self.max_depth = max(cur_depth, self.max_depth)
        cur_depth -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Get the maximum depth."""
        cur_depth = 0
        self.dfs(root, cur_depth)
        return self.max_depth
