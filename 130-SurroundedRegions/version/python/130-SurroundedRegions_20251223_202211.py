# Last updated: 12/23/2025, 8:22:11 PM
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
21            if board[r][0] == 'O':
22                dfs(r, 0)
23            if board[r][n - 1] == 'O':
24                dfs(r, n - 1)
25        
26        for c in range(n):
27            if board[0][c] == 'O':
28                dfs(0, c)
29            if board[m - 1][c] == 'O':
30                dfs(m-1, c)
31
32        for r in range(m):
33            for c in range(n):
34                if board[r][c] == 'O':
35                    board[r][c] = 'X'
36                elif board[r][c] == 'T':
37                    board[r][c] = 'O'
38                
39
40        