# Last updated: 8/31/2026, 7:25:10 PM
1class Solution:
2    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
3        n = len(matrix)
4        degrees = [0] * n
5
6        for i in range(n):
7            for j in range(n):
8                if i != j and matrix[i][j] == 1:
9                    degrees[i] += 1
10                    # degrees[j] += 1
11        
12        return degrees
13