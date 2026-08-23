# Last updated: 8/23/2026, 12:52:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8
9class Solution:
10    def rightSideView(self, root):
11        if not root:
12            return []
13        
14        right_view = []
15        q = deque([root])
16        
17        while q:
18            level_size = len(q)
19            for i in range(level_size):
20                node = q.popleft()
21                if i == level_size - 1:
22                    right_view.append(node.val)
23                if node.left:
24                    q.append(node.left)
25                if node.right:
26                    q.append(node.right)
27        
28        return right_view
29            