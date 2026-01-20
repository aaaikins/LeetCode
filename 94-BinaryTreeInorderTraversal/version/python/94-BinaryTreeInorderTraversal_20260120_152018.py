# Last updated: 1/20/2026, 3:20:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        res = []
11
12        def inorder(node):
13            if not node: return 
14            inorder(node.left)
15            res.append(node.val)
16            inorder(node.right)
17        
18        inorder(root)
19        return res