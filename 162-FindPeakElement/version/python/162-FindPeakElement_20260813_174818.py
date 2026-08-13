# Last updated: 8/13/2026, 5:48:18 PM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        if len(nums) <= 1:
4            return 0
5
6        l, r = 0, len(nums) - 1
7
8        while l < r:
9            m = (l + r) // 2
10            if nums[m] < nums[m + 1]:
11                l = m + 1
12            else:
13                r = m
14        
15        return l