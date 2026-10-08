# Last updated: 10/8/2026, 7:01:30 PM
1class Solution:
2    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
3        res = []
4
5
6        for start, end in intervals:
7            if end < newInterval[0]:
8                res.append([start, end])
9            elif start > newInterval[1]:
10                res.append(newInterval)
11                newInterval = [start, end]
12            else:
13                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
14        
15        res.append(newInterval)
16        
17        return res