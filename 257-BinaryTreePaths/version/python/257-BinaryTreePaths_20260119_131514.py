# Last updated: 1/19/2026, 1:15:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
9        res = []
10
11        def dfs(node, path):
12            if not node:
13                return " "
14            if not node.left and not node.right:
15                path += str(node.val)
16                res.append(path)
17            
18            path += str(node.val) + "->"
19
20            dfs(node.left, path)
21            dfs(node.right, path)
22
23        dfs(root, "")
24        return res
25
26
27