# Last updated: 1/20/2026, 4:40:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        if not root:
11            return []
12
13        res = []
14        node = root
15        stack = [node]
16
17        while stack:
18            node = stack.pop()
19            res.append(node.val)
20
21            if node.left:
22                stack.append(node.left)
23            if node.right:
24                stack.append(node.right)
25
26        return res[::-1]
27            