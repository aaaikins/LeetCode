# Last updated: 10/6/2026, 7:08:25 PM
1class Solution:
2    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
3        intervals.sort()
4        merged = [intervals[0]]
5
6        for s, e in intervals:
7            if merged[-1][-1] >= s:
8                merged[-1][-1] = max(merged[-1][-1], e)
9            else:
10                merged.append([s, e])
11        
12        return merged
13