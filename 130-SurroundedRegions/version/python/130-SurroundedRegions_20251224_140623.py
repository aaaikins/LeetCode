# Last updated: 12/24/2025, 2:06:23 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        m = len(board)
7        n = len(board[0])
8
9        def dfs(i, j):
10            if (i < 0 or i >= m) or (j < 0 or j >= n) or board[i][j] != 'O':
11                return 
12            
13            board[i][j] = 'T'
14
15            dfs(i + 1, j)
16            dfs(i, j + 1)
17            dfs(i - 1, j)
18            dfs(i, j - 1)
19        
20        for r in range(m):
21            for c in range(n):
22                if board[r][c] == 'O' and (r in [0, m - 1] or c in [0, n - 1]):
23                    dfs(r, c)
24
25        for r in range(m):
26            for c in range(n):
27                if board[r][c] == 'O':
28                    board[r][c] = 'X'
29                elif board[r][c] == 'T':
30                    board[r][c] = 'O'
31                
32
33        