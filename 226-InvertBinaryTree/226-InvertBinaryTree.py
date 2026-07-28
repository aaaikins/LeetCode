# Last updated: 7/28/2026, 5:08:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if root is None:
10            return None
11        
12        root.left, root.right = root.right, root.left
13
14        self.invertTree(root.left)
15        self.invertTree(root.right)
16    
17        return root
18
19        # def invert(node):
20        #     if node is None:
21        #         return None
22            
23        #     node.left, node.right = node.right, node.left
24
25        #     invert(node.left)
26        #     invert(node.right)
27
28        # invert(root)
29        # return root