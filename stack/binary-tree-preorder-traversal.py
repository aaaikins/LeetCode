# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            stack = [node]
            while stack:
                top = stack.pop()
                res.append(top.val)
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        
        dfs(root)
        return res