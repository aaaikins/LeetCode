# Last updated: 8/23/2026, 1:12:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        good_nodes = 0
10        # path_max = root.val
11
12        def dfs(node, path_max):
13            nonlocal good_nodes
14            if not node:
15                return 0
16            path_max = max(node.val, path_max)
17            if node.val >= path_max:
18                good_nodes += 1
19            dfs(node.left, path_max)
20            dfs(node.right, path_max)
21
22        dfs(root, root.val)
23        return good_nodes
24
25