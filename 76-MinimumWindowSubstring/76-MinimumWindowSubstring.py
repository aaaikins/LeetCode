# Last updated: 2/4/2026, 12:19:47 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if s == t:
4            return t
5        if len(s) < len(t):
6            return ""
7
8        need = Counter(t)
9        missing = len(t)
10
11        l = 0
12        minLen = float("inf")
13        start = 0
14
15        for r, ch in enumerate(s):
16            if need[ch] > 0:
17                missing -= 1
18            need[ch] -= 1
19
20            while missing == 0:
21                if (r - l + 1) < minLen:
22                    minLen = (r - l + 1)
23                    start = l
24                print(l)
25                need[s[l]] += 1
26                if need[s[l]] > 0:
27                    missing += 1
28                l += 1
29
30        return "" if minLen == float("inf") else s[start:start + minLen]
31
32
33
34
35
36        