# Last updated: 2/3/2026, 7:04:16 PM
1class Solution:
2    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(matrix), len(matrix[0])
4        result = [[0] * rows for _ in range(cols)]
5
6        for r in range(rows):
7            for c in range(cols):
8                result[c][r] = matrix[r][c]
9
10        return result
11
12
13