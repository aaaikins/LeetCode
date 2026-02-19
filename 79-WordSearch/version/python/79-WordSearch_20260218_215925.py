# Last updated: 2/18/2026, 9:59:25 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        nRows = len(board)
4        nCols = len(board[0])
5        path = set()
6
7        def dfs(r, c, idx):
8            if idx == len(word):
9                return True
10
11            if (r < 0 or r >= nRows) or (c < 0 or c >= nCols) or board[r][c] != word[idx] or (r,c) in path:
12                return False
13
14            path.add((r, c))
15            found = (
16            dfs(r + 1, c, idx + 1) or 
17            dfs(r - 1, c, idx + 1) or 
18            dfs(r, c + 1, idx + 1) or 
19            dfs(r, c - 1, idx + 1))
20
21            path.remove((r, c))
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