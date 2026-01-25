# Last updated: 1/25/2026, 4:03:45 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        nRows = len(board)
4        nCols = len(board[0])
5
6        exist = False
7
8        
9        def dfs(r, c, idx):
10            if idx == len(word):
11                return True
12
13            if (r < 0 or r >= nRows) or (c < 0 or c >= nCols) or board[r][c] != word[idx]:
14                return False
15        
16            temp = board[r][c]
17            board[r][c] = '#'
18            found = (
19            dfs(r + 1, c, idx + 1) or 
20            dfs(r - 1, c, idx + 1) or 
21            dfs(r, c + 1, idx + 1) or 
22            dfs(r, c - 1, idx + 1))
23
24            board[r][c] = temp
25
26            return found
27        
28
29        for r in range(nRows):
30            for c in range(nCols):
31                if dfs(r, c, 0):
32                    exist = True
33
34        return exist