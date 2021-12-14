"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/


Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


-> Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

-> Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

-> Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
1. The number of nodes in the tree is in the range [0, 5000].
2. -1000 <= Node.val <= 1000
3. -1000 <= targetSum <= 1000
"""
from collections import deque
from typing import Optional


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


class FindTargetSum(Exception):
    """Customize exception error."""

    pass


class Solution:
    target_sum = 0
    queue_sum = 0

    def dfs(self, root: Optional[TreeNode]) -> None:
        """Implement dfs."""
        if root:
            self.queue_sum += root.val

            # early stop condition
            if not root.left and not root.right and self.queue_sum == self.target_sum:
                raise FindTargetSum()

            self.dfs(root.left)
            self.dfs(root.right)

            self.queue_sum -= root.val

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Check if the sum of root-to-leaf pathn equals targetSum."""
        self.target_sum = targetSum if root else -1

        try:
            self.dfs(self.dfs(root))
        except FindTargetSum:
            return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Check if the sum of root-to-leaf pathn equals targetSum.

        Better solution.
        """
        if not root:
            return False

        queue = deque([root, 0])
        while queue:
            node, total = deque.popleft()
            total += node.val
            if not node.right and not node.left and total == targetSum:
                return True
            if node.left:
                deque.append((node.left, total))
            if node.right:
                deque.append((node.right, total))
        return False
