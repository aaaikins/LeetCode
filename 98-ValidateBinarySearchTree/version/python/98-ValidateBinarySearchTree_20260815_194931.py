# Last updated: 8/15/2026, 7:49:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9
10        def dfs(node, left, right):
11            if not node:
12                return True
13            if (node.val <= left) or (node.val >= right):
14                return False
15            
16            l = dfs(node.left, left, node.val)
17            r = dfs(node.right, node.val, right)
18
19            return l and r
20        
21        return dfs(root, -inf, inf)
22            
23        