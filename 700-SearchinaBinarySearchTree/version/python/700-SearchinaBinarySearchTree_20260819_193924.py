# Last updated: 8/19/2026, 7:39:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9
10        def dfs(node, val):
11            if not node:
12                return None
13            if val < node.val:
14                return dfs(node.left, val)
15            elif val > node.val:
16                return dfs(node.right, val)
17            else:
18                return node
19        
20        return dfs(root, val)