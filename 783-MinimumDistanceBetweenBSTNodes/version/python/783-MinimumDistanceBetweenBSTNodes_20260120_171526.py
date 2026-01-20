# Last updated: 1/20/2026, 5:15:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
9        min_diff = float("inf")
10        prev_val = None
11
12        def inorder(node):
13            nonlocal prev_val, min_diff
14            if not node:
15                return
16
17            inorder(node.left)
18
19            if prev_val is not None:
20                min_diff = min(min_diff, node.val - prev_val)
21
22            prev_val = node.val
23
24            inorder(node.right)
25
26        inorder(root)
27
28        return min_diff
29