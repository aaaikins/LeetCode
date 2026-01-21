# Last updated: 1/21/2026, 5:26:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
9        def postorder(node):
10            if not node:
11                return None
12
13            node.left = postorder(node.left)
14            node.right = postorder(node.right)
15
16            if not node.left and not node.right and node.val == target:
17                    return None
18
19            return node
20
21        return postorder(root)
22        # return root