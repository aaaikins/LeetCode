# Last updated: 9/2/2026, 6:21:15 PM
1class Solution:
2    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
3        res = []
4        q = deque([[0]])
5
6        while q:
7            path = q.popleft()
8            node = path[-1]
9
10            if node == len(graph) - 1:
11                res.append(path)
12                continue
13
14            for neighbor in graph[node]:
15                q.append(path + [neighbor])
16
17        return res