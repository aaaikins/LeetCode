# Last updated: 7/11/2026, 4:02:09 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for n in nums:
6            if n in seen:
7                return True
8            seen.add(n)
9
10        return False
11        