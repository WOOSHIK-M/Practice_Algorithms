"""
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


-> Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

-> Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

-> Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
1. The number of nodes in the tree is in the range [2, 105].
2. -10^9 <= Node.val <= 10^9
3. All Node.val are unique.
4. p != q
5. p and q will exist in the tree.
"""
# Definition for a binary tree node.
class TreeNode:
    """Tree Node class."""

    def __init__(self, x):
        """Initialize."""
        self.val = x
        self.left = None
        self.right = None


class Solution:
    queue = []
    p, q = None, None

    def dfs(self, root: TreeNode):
        """Implement customized dfs."""
        if root == self.p:
            return self.p
        if root == self.q:
            return self.q

        left, right = None, None
        if root.left:
            left = self.dfs(root.left)
        if root.right:
            right = self.dfs(root.right)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """Find the lowest common ancestor."""
        self.p, self.q = p, q
        return self.dfs(root)
