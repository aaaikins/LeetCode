# Last updated: 7/28/2026, 5:52:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        
10        def dfs(node):
11            if node is None:
12                return 0
13            
14            return max(dfs(node.left), dfs(node.right)) + 1
15
16        return dfs(root)