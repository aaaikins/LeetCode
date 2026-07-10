# Last updated: 7/10/2026, 6:36:41 PM
1class Solution:
2    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
3        ways = 0
4        pens = 0
5
6        while (pens * cost1) <= total:
7            remaining = total - (pens * cost1)
8            pencils = (remaining // cost2) + 1
9            ways += pencils
10            pens += 1
11
12        return ways 