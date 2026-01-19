# Last updated: 1/19/2026, 12:42:13 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        
10        def dfs(node, curSum):
11            if not node:
12                return False
13
14            curSum += node.val
15            if not node.left and not node.right:
16                return curSum == targetSum
17            
18
19            return dfs(node.left, curSum) or dfs(node.right, curSum)
20
21        return dfs(root, 0)