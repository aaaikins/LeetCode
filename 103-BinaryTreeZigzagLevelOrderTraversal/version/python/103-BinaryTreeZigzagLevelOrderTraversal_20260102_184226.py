# Last updated: 1/2/2026, 6:42:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11
12        q = deque([root])
13        res = []
14        rev = False
15
16        while q:
17            level = []
18            for _ in range(len(q)):
19                cur = q.popleft()
20                level.append(cur.val)
21
22                if cur.left:
23                    q.append(cur.left)
24                if cur.right:
25                    q.append(cur.right)
26            if not rev:
27                res.append(level)
28            else:
29                res.append(level[::-1])
30            rev = not rev
31
32        return res
33