# Last updated: 7/16/2026, 3:29:10 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l = 0
4        maxProfit = 0
5
6        for r in range(1, len(prices)):
7            curProfit = prices[r] - prices[l]
8            maxProfit = max(curProfit, maxProfit)
9
10            while l < r and prices[r] < prices[l]:
11                l += 1
12            
13        
14        return maxProfit