# Last updated: 7/11/2026, 4:09:40 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        seen = {}
4
5        for i, n in enumerate(nums):
6            if n in seen and abs(seen[n] - i) <= k:
7                return True
8            seen[n] = i
9        
10        return False