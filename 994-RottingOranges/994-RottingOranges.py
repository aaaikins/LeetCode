# Last updated: 1/4/2026, 7:41:57 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rotten = []
4
5        fresh = 0
6
7        nRows = len(grid)
8        nCols = len(grid[0])
9
10        for r in range(nRows):
11            for c in range(nCols):
12                if grid[r][c] == 2:
13                    rotten.append((r, c, 0))
14                if grid[r][c] == 1:
15                    fresh += 1
16
17        q = deque(rotten)
18        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
19        visited = set()
20        time = 0 
21
22        while q:
23            cur_r, cur_c, t = q.popleft()
24
25            for dr, dc in dirs:
26                nr, nc = cur_r + dr, cur_c + dc
27                if 0 <= nr < nRows and 0 <= nc < nCols and grid[nr][nc] == 1:
28                    grid[nr][nc] = 2
29                    fresh -= 1
30                    q.append((nr, nc, t + 1))
31            time = t
32
33        if fresh > 0:
34            return -1
35        
36        return time
37
38
39
40        
41