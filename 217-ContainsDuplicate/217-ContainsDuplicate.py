# Last updated: 10/17/2026, 7:56:09 PM
1class Solution:
2    def containsDuplicate(self, nums: list[int]) -> bool:
3        seen = set()
4
5        for num in nums:
6            if num in seen:
7                return True
8            else:
9                seen.add(num)
10            
11        return False