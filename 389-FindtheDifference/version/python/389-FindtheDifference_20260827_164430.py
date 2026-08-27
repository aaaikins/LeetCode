# Last updated: 8/27/2026, 4:44:30 PM
1class Solution:
2    def findTheDifference(self, s: str, t: str) -> str:
3        if not s:
4            return t
5        s = sorted(s)
6        t = sorted(t)
7
8        i = 0
9
10        while i < len(t):
11            if i >= len(s) or s[i] != t[i]:
12                    break
13            i += 1
14        
15        return t[i]