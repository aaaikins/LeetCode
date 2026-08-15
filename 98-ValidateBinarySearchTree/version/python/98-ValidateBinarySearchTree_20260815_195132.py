# Last updated: 8/15/2026, 7:51:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        
10
11        def dfs(node, left, right):
12            if not node:
13                return True
14            
15            if (node.val <= left) or (node.val >= right):
16                return False
17            
18            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
19
20        return dfs(root, -inf, inf)