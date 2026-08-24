# Last updated: 8/24/2026, 5:38:34 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        stones = [ -s for s in stones]
4        heapify(stones)
5
6        while len(stones) > 1:
7            x = heappop(stones)
8            y = heappop(stones)
9
10            if x != y:
11                heappush(stones, x - y)
12        
13        return -stones[0] if stones else 0