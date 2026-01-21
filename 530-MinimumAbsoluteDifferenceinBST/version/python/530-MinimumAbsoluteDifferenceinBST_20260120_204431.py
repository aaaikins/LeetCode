# Last updated: 1/20/2026, 8:44:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        min_diff = float("inf")
10        prev_val = -float("inf")
11
12        def inorder(node):
13            nonlocal prev_val, min_diff
14            if not node:
15                return
16
17            inorder(node.left)
18
19            min_diff = min(min_diff, node.val - prev_val)
20            prev_val = node.val
21
22            inorder(node.right)
23
24        inorder(root)
25        return min_diff