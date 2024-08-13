# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        results = set()

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            results.add(node.val)
            inorder(node.right)

        inorder(root)

        results = list(results)
        results.sort()

        if len(results) == 1:
            return -1
        else:
            return results[1]
        