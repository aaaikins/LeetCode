# Last updated: 8/23/2026, 1:16:13 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        good_nodes = 0
10
11        def dfs(node, path_max):
12            nonlocal good_nodes
13            if not node:
14                return None
15
16            if node.val >= path_max:
17                good_nodes += 1
18
19            path_max = max(node.val, path_max)
20
21            dfs(node.left, path_max)
22            dfs(node.right, path_max)
23
24        dfs(root, root.val)
25        return good_nodes
26
27