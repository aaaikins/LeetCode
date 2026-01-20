# Last updated: 1/20/2026, 3:33:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        node = root
11        stack = []
12
13        while node or stack:
14
15            while node:
16                stack.append(node)
17                node = node.left
18                
19            node = stack.pop()
20            res.append(node.val)
21
22            node = node.right
23        
24        return res
25        
26