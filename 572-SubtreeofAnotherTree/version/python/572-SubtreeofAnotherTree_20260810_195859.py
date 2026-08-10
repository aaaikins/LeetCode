# Last updated: 8/10/2026, 7:58:59 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9
10    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
11        if not subRoot:
12            return True
13        if not root:
14            return False
15
16        if self.sameTree(root, subRoot):
17            return True
18        return (self.isSubtree(root.left, subRoot) or
19               self.isSubtree(root.right, subRoot))
20
21    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
22        if not root and not subRoot:
23            return True
24        if root and subRoot and root.val == subRoot.val:
25            return (self.sameTree(root.left, subRoot.left) and
26                   self.sameTree(root.right, subRoot.right))
27        return False