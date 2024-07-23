# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []

        if not root:
            return
        queue.append(root)

        while len(queue) > 0:
            # curNode = queue.pop(0)
            nodeList = []
            for i in range(len(queue)):
                curNode = queue.pop(0)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                
                nodeList.append(curNode.val)
            res.append(nodeList)


        return res

        