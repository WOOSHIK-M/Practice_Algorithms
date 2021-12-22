"""
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/1016/


Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


-> Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

-> Example 2:
Input: root = []
Output: []

Constraints:
1. The number of nodes in the tree is in the range [0, 6000].
2. -100 <= Node.val <= 100

Follow-up:
1. You may only use constant extra space.
2. The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
from collections import deque


# Definition for a Node.
class Node:
    """Node class."""

    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        """Initialize."""
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        """Make a connection."""
        if not root:
            return root

        level = 0
        queue = deque([(level, root)])
        while queue:
            level, head = queue.popleft()

            if head.left:
                queue.append((level + 1, head.left))
            if head.right:
                queue.append((level + 1, head.right))
            if queue and level == queue[0][0]:
                head.next = queue[0][1]
        return root
