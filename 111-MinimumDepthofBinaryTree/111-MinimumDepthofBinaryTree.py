# Last updated: 7/28/2026, 6:39:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: Optional[TreeNode]) -> int:
9        if root is None:
10            return 0
11
12        
13        q = deque([root])
14        # minHeight = inf
15        level = 1
16
17        while q:
18            for _ in range(len(q)):
19                cur = q.popleft()
20                if cur.left is None and cur.right is None:
21                    return level
22
23                if cur.left:
24                    q.append(cur.left)
25                if cur.right:
26                    q.append(cur.right)
27
28            level += 1
29            
30            # minHeight = min(minHeight, level)
31        
32        return minHeight
33
34                    
35