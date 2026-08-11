# Last updated: 8/11/2026, 5:56:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def helper(node):
11            if p.val < node.val and q.val < node.val:
12                return helper(node.left)
13            elif p.val > node.val and q.val > node.val:
14                return helper(node.right)
15            else:
16                return node
17            
18        return helper(root)
19