# Last updated: 1/22/2026, 2:12:16 PM
1class Solution:
2    def findCenter(self, edges: List[List[int]]) -> int:
3        u1, v1 = edges[0]
4        u2, v2 = edges[1]
5
6        return u1 if u1 == u2 or u1 == v2 else v1