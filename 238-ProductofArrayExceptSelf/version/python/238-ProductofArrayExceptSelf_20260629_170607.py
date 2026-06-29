# Last updated: 6/29/2026, 5:06:07 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        res = [1] * n
5
6        l = 1
7        for i in range(n):
8            res[i] *= l
9            l *= nums[i]
10            
11        r = 1
12        for i in range(n-1, -1, -1):
13            res[i] *= r
14            r *= nums[i]
15
16        return res