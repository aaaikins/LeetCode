# Last updated: 1/25/2026, 4:04:21 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        nRows = len(board)
4        nCols = len(board[0])
5
6        def dfs(r, c, idx):
7            if idx == len(word):
8                return True
9
10            if (r < 0 or r >= nRows) or (c < 0 or c >= nCols) or board[r][c] != word[idx]:
11                return False
12        
13            temp = board[r][c]
14            board[r][c] = '#'
15            found = (
16            dfs(r + 1, c, idx + 1) or 
17            dfs(r - 1, c, idx + 1) or 
18            dfs(r, c + 1, idx + 1) or 
19            dfs(r, c - 1, idx + 1))
20
21            board[r][c] = temp
22
23            return found
24        
25
26        for r in range(nRows):
27            for c in range(nCols):
28                if dfs(r, c, 0):
29                    return True
30
31        return False