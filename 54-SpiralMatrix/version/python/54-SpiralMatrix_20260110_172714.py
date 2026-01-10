# Last updated: 1/10/2026, 5:27:14 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        top, bottom = 0, len(matrix)
4        left, right = 0, len(matrix[0])
5
6        res = []
7
8        while left < right and top < bottom:
9            for a in range(left, right):
10                res.append(matrix[top][a])
11            top += 1
12
13            for b in range(top, bottom):
14                res.append(matrix[b][right - 1])
15            right -= 1
16            
17            if left < right and top < bottom:
18                for c in range(right -1, left - 1, -1):
19                    res.append(matrix[bottom - 1][c])
20                bottom -= 1
21
22                for d in range(bottom - 1, top - 1, -1):
23                    res.append(matrix[d][left])
24                left += 1
25
26        return res
27
28
29