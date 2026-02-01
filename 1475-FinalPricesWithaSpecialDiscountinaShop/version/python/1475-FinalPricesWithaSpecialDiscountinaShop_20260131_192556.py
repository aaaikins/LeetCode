# Last updated: 1/31/2026, 7:25:56 PM
1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        n = len(prices)
4        res = prices[:]
5
6        stack = []
7
8        for i, p in enumerate(prices):
9            while stack and p <= stack[-1][1]:
10                cur_i, cur_p = stack.pop()
11                res[cur_i] = cur_p - p
12
13            stack.append((i, p))
14        
15        return res
16        