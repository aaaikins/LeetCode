# Last updated: 10/20/2026, 7:06:44 PM
1class Solution:
2    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
3        
4        graph = defaultdict(list)
5
6        for u, v, w in times:
7            graph[u].append((v, w))
8
9        dist = {i: float('inf') for i in range(1, n + 1)}
10        dist[k] = 0
11
12        min_heap = [(0, k)]
13
14        while min_heap:
15            d, node = heapq.heappop(min_heap)
16
17            if d > dist[node]:
18                continue
19
20            for nei, weight in graph[node]:
21                
22                new_dist = d + weight
23
24                if new_dist < dist[nei]:
25                    dist[nei] = new_dist
26                    heapq.heappush(min_heap, (new_dist, nei))
27        print(dist)
28        res = max(dist.values())
29
30        return res if res != float('inf') else -1
31