# Last updated: 9/19/2026, 10:47:27 PM
1class Solution:
2    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
3        m = len(image)
4        n = len(image[0])
5
6        start = image[sr][sc]
7        if start == color:
8            return image
9
10        def dfs(r, c):
11            if (r < 0 or r >= m) or (c < 0 or c >= n) or image[r][c] != start:
12                return
13            
14            image[r][c] = color
15            dfs(r + 1, c)
16            dfs(r-1, c)
17            dfs(r, c + 1)
18            dfs(r, c - 1)
19
20            # return image
21        
22        dfs(sr, sc)
23        return image