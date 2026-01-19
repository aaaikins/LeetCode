# Last updated: 1/19/2026, 1:41:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
9
10        def dfs(node, isLeft):
11            if not node: return 0
12
13            if not node.left and not node.right and isLeft:
14                return node.val
15            
16            return dfs(node.left, True) + dfs(node.right, False)
17
18        return dfs(root, False)
19
20
21        