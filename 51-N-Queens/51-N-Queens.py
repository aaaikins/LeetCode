# Last updated: 10/18/2026, 6:42:07 PM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        cols = set()
4        posDiag = set()
5        negDiag = set()
6
7        result = []
8        board = [["."] * n for i in range(n)]
9
10        def backtrack(r):
11            if r == n:
12                copy = ["".join(row) for row in board]
13                result.append(copy)
14                return
15            
16            for c in range(n):
17                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
18                    continue
19
20                cols.add(c)
21                posDiag.add(r + c)
22                negDiag.add(r - c)
23                board[r][c] = "Q"
24
25                backtrack(r + 1)
26
27                cols.remove(c)
28                posDiag.remove(r + c)
29                negDiag.remove(r - c)
30                board[r][c] = "."
31
32        backtrack(0)
33        return result