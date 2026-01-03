# Last updated: 1/2/2026, 7:26:09 PM
1class Solution:
2    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
3        nRows = len(grid)
4        nCols = len(grid[0])
5        res = []
6
7        r = 0
8        while r < nRows:
9            if r % 2 == 0:
10                for c in range(nCols):
11                    if c % 2 == 0:
12                        res.append(grid[r][c])
13            else:
14                for c in range(nCols-1, -1, -1):
15                    if c % 2 == 1:
16                        res.append(grid[r][c])
17
18            r += 1
19
20            
21        
22        return res