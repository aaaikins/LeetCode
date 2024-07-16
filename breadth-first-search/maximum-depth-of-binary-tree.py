# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_left_dept = self.maxDepth(root.left)
        max_right_dept = self.maxDepth(root.right)
        
        return 1 + max(max_left_dept, max_right_dept)
        