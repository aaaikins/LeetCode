# Last updated: 7/27/2026, 7:22:30 PM
1from collections import Counter
2
3class Solution:
4    def findValidPair(self, s: str) -> str:
5        count = Counter(s)
6        for i in range(len(s) - 1):
7            a, b = s[i], s[i + 1]
8            if a != b and count[a] == int(a) and count[b] == int(b):
9                return a + b
10        return ""
11
12
13        