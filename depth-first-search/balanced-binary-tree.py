# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def maxDepth(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            return 1+ max(left, right)
        
        def dfs(root):
            if not root: return True
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return abs(left-right) <= 1 and dfs(root.left) and dfs(root.right)
        
        return dfs(root)

        
        
        