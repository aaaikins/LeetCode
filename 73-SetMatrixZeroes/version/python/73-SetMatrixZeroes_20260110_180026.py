# Last updated: 1/10/2026, 6:00:26 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        rowZero = False
7        colZero = False
8
9        nRows = len(matrix)
10        nCols = len(matrix[0])
11
12        for r in range(nRows):
13            if matrix[r][0] == 0:
14                colZero = True
15        
16        for c in range(nCols):
17            if matrix[0][c] == 0:
18                rowZero = True
19
20        for r in range(nRows):
21            for c in range(nCols):
22                if matrix[r][c] == 0:
23                    matrix[r][0] = 0
24                    matrix[0][c] = 0
25        
26        for r in range(1, nRows):
27            for c in range(1, nCols):
28                if matrix[r][0] == 0:
29                    matrix[r][c] = 0
30                if matrix[0][c] == 0:
31                    matrix[r][c] = 0
32        
33        if rowZero:
34            for c in range(nCols):
35                matrix[0][c] = 0
36        
37        if colZero:
38            for r in range(nRows):
39                matrix[r][0] = 0
40                