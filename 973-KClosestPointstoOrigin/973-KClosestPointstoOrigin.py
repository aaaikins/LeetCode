# Last updated: 8/25/2026, 3:50:46 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        heap = []
4
5        for p in points:
6            x, y = p
7            dist = x**2 + y**2
8
9            heap.append((dist, p))
10        
11        heapify(heap)
12
13        res = []
14
15        while len(res) < k:
16            dist, p = heappop(heap)
17            res.append(p)
18        
19        return res