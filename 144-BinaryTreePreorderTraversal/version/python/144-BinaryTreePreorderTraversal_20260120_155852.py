# Last updated: 1/20/2026, 3:58:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10
11        def preorder(node):
12            if not node:
13                return
14            
15            res.append(node.val)
16            preorder(node.left)
17            preorder(node.right)
18        
19        preorder(root)
20        return res