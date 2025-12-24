# Last updated: 12/23/2025, 7:28:45 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        """
4        pacific ocean : left and top
5        atlantic ocean: right and bottom
6        inputs: heights(matrix), height[r][c] -> height above sea level
7
8        water can flow: east, west, north, south
9        water can flow if neighbor <= cur cell heoght
10
11        output: 2d grid of positions where water can flow
12        """
13        m = len(heights)
14        n = len(heights[0])
15        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
16
17        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
18        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
19
20
21        def bfs(starts):
22            visited = set(starts)
23            q = deque(starts)
24
25            while q:
26                r, c = q.popleft()
27                for dr, dc in dirs:
28                    nr, nc = r + dr, c + dc
29                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
30                        if heights[nr][nc] >= heights[r][c]:
31                            visited.add((nr, nc))
32                            q.append((nr, nc))
33            
34            return visited
35
36
37        pac = bfs(pacific_starts)
38        atl = bfs(atlantic_starts)
39        
40        return [[r, c]  for r, c in pac & atl]
41
42
43
44
45
46