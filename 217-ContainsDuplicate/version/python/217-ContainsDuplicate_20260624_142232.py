# Last updated: 6/24/2026, 2:22:32 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for n in nums:
6            if n in seen:
7                return True
8            
9            seen.add(n)
10        
11        return False
12        