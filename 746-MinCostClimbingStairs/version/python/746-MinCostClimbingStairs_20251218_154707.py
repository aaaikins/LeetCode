# Last updated: 12/18/2025, 3:47:07 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n = len(cost)
4        dp = [0] * (n + 2)
5        dp[n - 1] = 0
6
7        for i in range(n - 1, -1, -1):
8            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
9        
10        return min(dp[0], dp[1])
11