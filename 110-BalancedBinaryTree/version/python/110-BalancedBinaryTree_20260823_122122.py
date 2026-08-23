# Last updated: 8/23/2026, 12:21:22 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced = True
10        def dfs(node):
11            nonlocal balanced
12            if not node:
13                return 0
14
15            l = dfs(node.left)
16            r = dfs(node.right)
17            balanced = balanced and abs(l - r) <= 1
18            return max(l, r) + 1
19        
20        dfs(root)
21        return balanced
22
23
24        