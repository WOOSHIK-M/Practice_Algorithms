"""
https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/


Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


-> Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

-> Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1. 1 <= n <= 8
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """Generate trees."""
        return self.get_trees(1, n)

    def get_trees(self, start, end):
        tree: List[TreeNode] = []
        if start > end:
            tree.append(None)
            return tree

        if start == end:
            tree.append(TreeNode(start))
            return tree

        for i in range(start, end + 1):
            left = self.get_trees(start, i - 1)
            right = self.get_trees(i + 1, end)

            for left_node in left:
                for right_node in right:
                    root = TreeNode(i, left=left_node, right=right_node)
                    tree.append(root)
        return tree
