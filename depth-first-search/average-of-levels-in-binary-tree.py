# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []
        res = []

        queue.append(root)
        while len(queue) > 0:
            total = []
            for i in range(len(queue)):
                curNode = queue.pop(0)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                total.append(curNode.val)
            res.append(sum(total)/len(total))
        
        return res
        