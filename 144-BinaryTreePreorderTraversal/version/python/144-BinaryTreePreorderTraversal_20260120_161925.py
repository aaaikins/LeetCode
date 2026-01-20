# Last updated: 1/20/2026, 4:19:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        stack = []
11
12        if not root:
13            return []
14        
15        node = root
16        stack.append(root)
17
18        while stack:
19            node = stack.pop()
20            res.append(node.val)
21
22            if node.right:
23                stack.append(node.right)
24            if node.left:
25                stack.append(node.left)
26        
27        return res