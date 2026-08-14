# Last updated: 8/14/2026, 3:29:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if root is None:
10            return []
11
12        q = deque([root])
13        result = []
14
15        while q:
16            level = []
17            for _ in range(len(q)):
18                cur = q.popleft()
19                if cur.left:
20                    q.append(cur.left)
21                if cur.right:
22                    q.append(cur.right)
23                level.append(cur.val)
24            result.append(level)
25        
26        return result
27                
28        