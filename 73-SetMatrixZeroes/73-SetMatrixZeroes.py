# Last updated: 1/5/2026, 3:43:46 PM
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
14        for c in range(nCols):
15            if matrix[0][c] == 0:
16                rowZero = True
17
18        for r in range(1, nRows):
19            for c in range(1, nCols):
20                if matrix[r][c] == 0:
21                    matrix[0][c] = 0
22                    matrix[r][0] = 0
23
24        for r in range(1, nRows):
25            for c in range(1, nCols):
26                if matrix[r][0] == 0 or matrix[0][c] == 0:
27                    matrix[r][c] = 0
28
29        # Fix: only zero first column if needed
30        if colZero:
31            for r in range(nRows):
32                matrix[r][0] = 0
33
34        if rowZero:
35            for c in range(nCols):
36                matrix[0][c] = 0
37