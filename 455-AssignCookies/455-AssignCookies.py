# Last updated: 10/15/2026, 5:51:22 PM
1class Solution:
2    def findContentChildren(self, g: list[int], s: list[int]) -> int:
3        g.sort()
4        s.sort()
5        i, j = 0, 0
6        content = 0
7
8        while i < len(g) and j < len(s):
9            if s[j] >= g[i]:
10                content += 1
11                i += 1
12            j += 1
13
14        
15        return content