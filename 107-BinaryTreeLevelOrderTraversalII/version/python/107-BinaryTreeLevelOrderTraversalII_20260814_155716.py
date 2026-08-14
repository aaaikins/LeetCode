# Last updated: 8/14/2026, 3:57:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
9        
10        if root is None:
11            return 0
12
13        q = deque([root])
14        result = []
15
16        while q:
17            n = len(q)
18            level = 0
19            for _ in range(n):
20                cur = q.popleft()
21                if cur.left:
22                    q.append(cur.left)
23                if cur.right:
24                    q.append(cur.right)
25                level += cur.val
26            result.append(level/n)
27        
28        return result