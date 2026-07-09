# Last updated: 7/9/2026, 7:57:31 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        nums = set(nums)
5        res = []
6
7        for i in range(1, n + 1):
8            if i not in nums:
9                res.append(i)
10        
11        return res
12
13
14        