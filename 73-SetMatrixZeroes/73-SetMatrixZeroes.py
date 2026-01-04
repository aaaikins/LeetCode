# Last updated: 1/4/2026, 6:02:52 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        nRows= len(matrix)
7        nCols= len(matrix[0])
8
9        zeros = set()
10
11        for r in range(nRows):
12            for c in range(nCols):
13                if matrix[r][c] == 0:
14                    zeros.add((r, c))
15        
16        # print(zeros)
17
18        for pos in zeros:
19            cur_r, cur_c = pos
20            for r in range(nRows):
21                matrix[r][cur_c] = 0
22            for c in range(nCols):
23                matrix[cur_r][c] = 0
24        
25        