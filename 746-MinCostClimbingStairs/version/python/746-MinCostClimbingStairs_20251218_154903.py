# Last updated: 12/18/2025, 3:49:03 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n = len(cost)
4        dp = [0] * (n + 2)
5        dp[n - 1] = 0
6        a, b = 0, 0
7
8        for i in range(n - 1, -1, -1):
9            # dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
10            a, b = b, cost[i] + min(a, b)
11        
12        # return min(dp[0], dp[1])
13        return min(a, b)
14