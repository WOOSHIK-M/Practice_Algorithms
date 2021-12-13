"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/


Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


-> Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

-> Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
1. The number of nodes in the tree is in the range [1, 1000].
2. -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
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
    def recursive(
        self, left_child: Optional[TreeNode], right_child: Optional[TreeNode]
    ) -> bool:
        """Check the childs recursively."""
        if not left_child and not right_child:
            return True
        elif not left_child or not right_child:
            return False
        else:
            return (
                left_child.val == right_child.val
                and self.recursive(left_child.left, right_child.right)
                and self.recursive(left_child.right, right_child.left)
            )

    def iterative(self, root: Optional[TreeNode]) -> bool:
        """Check the childs iteratively."""
        queue = deque([root, root])
        while queue:
            left, right = queue.popleft(), queue.popleft()

            if not left and not right:
                continue
            elif not left or not right:
                return False
            else:
                if left.val == right.val:
                    queue.extend([left.left, right.right, left.right, right.left])
                else:
                    return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check whether it is a mirror of itself."""
        return self.recursive(root.left, root.right)
        return self.iterative(root)
