# Last updated: 7/4/2026, 1:51:48 PM
1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3        l, r = 1, max(nums)
4
5        while l < r:
6            m = (l + r) // 2
7            total = sum(math.ceil(num/m) for num in nums)
8            if total <= threshold:
9                r = m
10            else:
11                l = m + 1
12
13        return l
14
15        
16