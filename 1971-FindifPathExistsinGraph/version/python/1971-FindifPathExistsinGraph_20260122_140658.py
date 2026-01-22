# Last updated: 1/22/2026, 2:06:58 PM
1class Solution:
2    def findCenter(self, edges: List[List[int]]) -> int:
3        graph = defaultdict(list)
4
5        for u, v in edges:
6            graph[u].append(v)
7            graph[v].append(u)
8        
9        for n in graph:
10            if len(graph[n]) == len(edges):
11                return n
12