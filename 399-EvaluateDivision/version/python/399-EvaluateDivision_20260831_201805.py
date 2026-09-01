# Last updated: 8/31/2026, 8:18:05 PM
1class Solution:
2    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
3        graph = defaultdict(list)
4        
5        for i in range(len(values)):
6            a, b = equations[i]
7            w = values[i]
8            graph[a].append((b, w))
9            graph[b].append((a, 1/w))
10
11        n = len(queries)
12        res = [-1] * n
13        for i in range(n):
14            start, end = queries[i]
15
16            if start not in graph or end not in graph:
17                res[i] = -1
18                continue
19
20            if start == end:
21                res[i] = 1
22                continue
23
24            q = deque([(start, 1.0)])
25            visited = {start}
26            # found = False
27
28            while q:
29                node, prod = q.popleft()
30                if node == end:
31                    res[i] = prod
32                    break
33
34                for neighbor, weight in graph[node]:
35                    if neighbor not in visited:
36                        visited.add(neighbor)
37                        q.append((neighbor, prod * weight))
38   
39        
40        return res