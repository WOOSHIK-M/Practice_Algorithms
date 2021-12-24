"""
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as **how LeetCode serializes a binary tree**. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


-> Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

-> Example 2:
Input: root = []
Output: []

Constraints:
1. The number of nodes in the tree is in the range [0, 10^4].
2. -1000 <= Node.val <= 1000
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    """Tree Node class."""

    def __init__(self, x):
        """Initialize."""
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "x"
        return ",".join(
            [str(root.val), self.serialize(root.left), self.serialize(root.right)]
        )

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = deque()
        queue.extend(data.split(","))
        self.data = queue
        root = self._deserialize()
        return root

    def _deserialize(self) -> TreeNode:
        """Helper function of Deserialization."""
        if self.data[0] == "x":
            self.data.popleft()
            return None
        node = TreeNode(self.data.popleft())
        node.left = self._deserialize()
        node.right = self._deserialize()
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
