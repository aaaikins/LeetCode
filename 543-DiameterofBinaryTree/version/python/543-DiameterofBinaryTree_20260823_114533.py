# Last updated: 8/23/2026, 11:45:33 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9
10        diameter = 0
11        def dfs(node):
12            nonlocal diameter
13            if not node:
14                return 0
15
16            l = dfs(node.left) 
17            r = dfs(node.right)
18
19            diameter = max(diameter, l + r)
20
21            return max(l, r) + 1
22
23        dfs(root)
24        return diameter