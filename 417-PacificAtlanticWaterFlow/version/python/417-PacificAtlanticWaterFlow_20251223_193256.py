# Last updated: 12/23/2025, 7:32:56 PM
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
12
13        approach:
14        1. build list of starting cells for both the pacific and atlantic ocean
15        2. Create a bfs helper that tranverses the grid inwardly (i.e. neighbor height >= current cell height)
16        3. perform bfs on both pacific and atlantic ocean starters 
17        4. return a list of the intersection of cells
18        """
19        m = len(heights)
20        n = len(heights[0])
21        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
22
23        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
24        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
25
26
27        def bfs(starts):
28            visited = set(starts)
29            q = deque(starts)
30
31            while q:
32                r, c = q.popleft()
33                for dr, dc in dirs:
34                    nr, nc = r + dr, c + dc
35                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
36                        if heights[nr][nc] >= heights[r][c]:
37                            visited.add((nr, nc))
38                            q.append((nr, nc))
39            
40            return visited
41
42
43        pac = bfs(pacific_starts)
44        atl = bfs(atlantic_starts)
45        
46        return [[r, c]  for r, c in pac & atl]
47
48
49
50
51
52