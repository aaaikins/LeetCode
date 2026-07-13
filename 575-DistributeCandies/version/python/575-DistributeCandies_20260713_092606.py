# Last updated: 7/13/2026, 9:26:06 AM
1class Solution:
2    def distributeCandies(self, candyType: List[int]) -> int:
3        n = len(candyType)
4        count = Counter(candyType)
5        
6        if len(count) <= n // 2:
7            return len(count)
8        else:
9            return n // 2