# Last updated: 12/18/2025, 3:52:11 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        next1, next2 = 0, 0
4
5        for i in range(len(cost) - 1, -1, -1):
6            curr = cost[i] + min(next1, next2)
7            next2 = next1
8            next1 = curr
9
10        return min(next1, next2)
11
12