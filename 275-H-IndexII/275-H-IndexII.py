# Last updated: 8/25/2026, 4:37:30 PM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        citations.sort(reverse=True)
4        h = 0
5        for c in citations:
6            if c < h + 1:
7                break
8            h += 1
9        return h