# Last updated: 7/28/2026, 5:46:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def maxDepth(self, root: Optional[TreeNode]) -> int:
10        if root is None:
11            return 0
12
13        q = deque([root])
14        level = 0
15        while q:
16            for _ in range(len(q)):
17                cur = q.popleft()
18                if cur.left:
19                    q.append(cur.left)
20                if cur.right:
21                    q.append(cur.right)
22            
23            level += 1
24
25        return level
26
27
28        