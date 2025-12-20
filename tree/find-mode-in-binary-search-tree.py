# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:


        def bfs(node):
            val = -inf
            cnt = 0
            q = deque([node])

            while q:
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
                if val == cur.val:
                    cnt += 1
                val = cur.val
                cnt += 1
            
            return val 
        
        return [bfs(root)]

            