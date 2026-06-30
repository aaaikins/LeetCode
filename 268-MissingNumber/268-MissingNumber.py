# Last updated: 6/30/2026, 10:44:26 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        numSet = set(nums)
6
7        for i in range(n + 1):
8            if i not in numSet:
9                return i
10        