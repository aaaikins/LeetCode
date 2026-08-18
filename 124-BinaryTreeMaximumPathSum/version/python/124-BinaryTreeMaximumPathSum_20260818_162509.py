# Last updated: 8/18/2026, 4:25:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res = -float("inf")
10
11        def dfs(node):
12            nonlocal res
13            if node is None:
14                return 0
15            
16            leftMax = max(dfs(node.left), 0)
17            rightMax = max(dfs(node.right), 0)
18
19            res = max(res, node.val + leftMax + rightMax)
20
21            return node.val + max(leftMax, rightMax)
22
23        dfs(root)
24
25        return res
26        