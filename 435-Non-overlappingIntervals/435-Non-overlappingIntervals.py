# Last updated: 10/7/2026, 7:47:38 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
3        intervals.sort()
4        count = 0
5        prev_end = intervals[0][1]
6
7        for start, end in intervals[1:]:
8            if start < prev_end:
9                count += 1
10                prev_end = min(prev_end, end)
11            else:
12                prev_end = end
13
14        return count