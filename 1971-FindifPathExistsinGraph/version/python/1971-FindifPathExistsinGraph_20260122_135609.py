# Last updated: 1/22/2026, 1:56:09 PM
1class Solution:
2    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
3        if source == destination:
4            return True
5
6        if not edges:
7            return False
8
9        graph = defaultdict(list)
10
11        for u, v in edges:
12            graph[u].append(v)
13            graph[v].append(u)
14
15        q = deque([source])
16        visit = set()
17
18        while q:
19            cur_node = q.popleft()
20
21            if cur_node in visit:
22                continue
23
24            visit.add(cur_node)
25
26            for neighbor in graph[cur_node]:
27                if neighbor == destination:
28                    return True
29                if neighbor not in visit:
30                    q.append(neighbor)
31        
32
33        return False
34
35