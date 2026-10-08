# Last updated: 10/8/2026, 6:31:04 PM
1class Solution:
2    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
3        intervals.append(newInterval)
4        intervals.sort()
5
6        new_intervals = [intervals[0]]
7        i = 0
8        for start, end in intervals[1:]:
9            # start, end = intervals[i]
10            if new_intervals[-1][-1] >= start:
11                new_intervals[-1][-1] = max(new_intervals[-1][-1], end)
12            else:
13                new_intervals.append([start, end])
14            # i += 1
15        return new_intervals
16
17