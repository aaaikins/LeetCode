# Last updated: 9/19/2026, 7:49:41 PM
1class Solution:
2    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(img), len(img[0])
4        result = [[0] * cols for _ in range(rows)]
5
6        for r in range(rows):
7            for c in range(cols):
8                total = 0
9                count = 0
10
11                for dr in (-1, 0, 1):
12                    for dc in (-1, 0, 1):
13                        nr, nc = r + dr, c + dc
14
15                        if 0 <= nr < rows and 0 <= nc < cols:
16                            total += img[nr][nc]
17                            count += 1
18
19                result[r][c] = total // count
20
21        return result