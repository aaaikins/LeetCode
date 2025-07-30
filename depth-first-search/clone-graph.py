"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def bfs(current):
            queue = [current]
            while queue:
                temp = queue.pop(0)
                if temp in visited:
                    return visited[temp]

                
                clone = Node(temp.val)
                visited[temp] = clone

                for n in temp.neighbors:
                    clone.neighbors.append(bfs(n))
            return clone
        
        

        return bfs(node)
        