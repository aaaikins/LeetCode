# Last updated: 10/15/2026, 5:33:57 PM
1class Solution:
2    def findContentChildren(self, g: list[int], s: list[int]) -> int:
3        g.sort()
4        s.sort()
5        i, j = 0, 0
6        content = 0
7
8        while i < len(g) and j < len(s):
9            # print('i', i)
10            # print('j', j)
11            if s[j] >= g[i]:
12                content += 1
13                j += 1
14                i += 1
15            else:
16                j += 1
17        # print(g)
18        # print(s)
19            # j += 1
20            # i += 1
21        
22        return content