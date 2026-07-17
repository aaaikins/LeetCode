# Last updated: 7/16/2026, 8:59:25 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        prefix = [1] * n
5
6        for i in range(n - 1):
7            prefix[i + 1] *= nums[i] * prefix[i]
8
9        suffix = [1] * n
10
11        for j in range(n -1, 0, -1):
12            suffix[j - 1] *= nums[j] * suffix[j]
13
14        res = []
15        for i in range(n):
16            res.append(prefix[i] * suffix[i])
17        
18        return res