# Last updated: 1/4/2026, 7:02:09 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        nRows = len(matrix)
4        nCols = len(matrix[0])
5
6        rowZero = False
7        colZero = False
8
9        # Check first column separately
10        for r in range(nRows):
11            if matrix[r][0] == 0:
12                colZero = True
13
14        for r in range(nRows):
15            for c in range(nCols):
16                if matrix[r][c] == 0:
17                    matrix[0][c] = 0
18                    if r > 0:
19                        matrix[r][0] = 0
20                    else:
21                        rowZero = True
22
23        for r in range(1, nRows):
24            for c in range(1, nCols):
25                if matrix[r][0] == 0 or matrix[0][c] == 0:
26                    matrix[r][c] = 0
27
28        # Fix: only zero first column if needed
29        if colZero:
30            for r in range(nRows):
31                matrix[r][0] = 0
32
33        if rowZero:
34            for c in range(nCols):
35                matrix[0][c] = 0
36