# Last updated: 7/13/2026, 9:28:58 AM
1class Solution:
2    def distributeCandies(self, candyType: List[int]) -> int:
3        n = len(candyType)
4        count = Counter(candyType)
5        
6        return min(len(count), n // 2)