# Last updated: 7/28/2026, 7:02:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if root is None:
10            return []
11        
12        q = deque([root])
13        res = []
14
15        while len(q) > 0:
16            level = []
17            for _ in range(len(q)):
18                cur = q.popleft()
19                level.append(cur.val)
20
21                if cur.left:
22                    q.append(cur.left)
23                if cur.right:
24                    q.append(cur.right)
25                
26            res.append(level)
27        
28        return res[::-1]