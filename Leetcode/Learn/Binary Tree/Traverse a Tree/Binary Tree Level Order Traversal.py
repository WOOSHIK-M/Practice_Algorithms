"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/


Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


-> Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

-> Example 2:
Input: root = [1]
Output: [[1]]

-> Example 3:
Input: root = []
Output: []

Constraints:
1. The number of nodes in the tree is in the range [0, 2000].
2. -1000 <= Node.val <= 1000
"""
from collections import defaultdict, deque
from typing import DefaultDict, Deque, List, Optional, Tuple


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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Level Order."""
        dic: DefaultDict[int, List[TreeNode]] = defaultdict(list)

        # tuple(levle, TreeNode)
        queue: Deque[Tuple[int, TreeNode]] = deque([(0, root)])

        while root and queue:
            level, node = queue.popleft()
            dic[level].append(node.val)

            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        return [dic[level] for level in sorted(dic)]
