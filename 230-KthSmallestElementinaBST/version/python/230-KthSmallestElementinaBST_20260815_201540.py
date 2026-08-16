# Last updated: 8/15/2026, 8:15:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        
10        count = 0
11        val = 0
12
13        def inorder(node):
14            nonlocal count, val
15            if not node:
16                return 
17
18            inorder(node.left)
19
20            count += 1
21            if count == k:
22                val = node.val
23
24            inorder(node.right)
25        
26        inorder(root)
27
28        return val
29