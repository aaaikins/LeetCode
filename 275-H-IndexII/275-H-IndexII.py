# Last updated: 8/25/2026, 5:03:17 PM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        n = len(citations)
4        l, r = 0, n - 1
5        h = 0
6
7        while l <= r:
8            m = (l + r) // 2
9            if citations[m] >= n - m:
10                h = n - m
11                r = m - 1
12            else:
13                l = m + 1
14
15        return h