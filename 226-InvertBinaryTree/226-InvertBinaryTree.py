# Last updated: 7/28/2026, 5:06:37 PM
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
12        def invert(node):
13            if node is None:
14                return None
15            
16            node.left, node.right = node.right, node.left
17
18            invert(node.left)
19            invert(node.right)
20
21        invert(root)
22        return root