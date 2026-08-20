# Last updated: 8/20/2026, 3:47:22 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
9
10        def dfs(node1, node2):
11            if not node1:
12                return node2
13            if not node2:
14                return node1
15                
16            node = TreeNode(node1.val + node2.val)
17
18            node.left = dfs(node1.left, node2.left)
19            node.right = dfs(node1.right, node2.right)
20
21            return node
22        
23        return dfs(root1, root2)
24
25        