# Last updated: 8/30/2026, 7:58:15 PM
1class Solution:
2    def toLowerCase(self, s: str) -> str:
3        results = []
4
5        for ch in s:
6            if 'A' <= ch <= 'Z':
7                results.append(chr(ord(ch) + 32))
8            else:
9                results.append(ch)
10        
11        return "".join(results)