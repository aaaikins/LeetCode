# Last updated: 8/6/2026, 4:41:07 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4
5        res = nums[l]
6
7        while l < r:
8            m = (l + r) // 2
9            if nums[l] < nums[r]:
10                res = min(res, nums[l])
11                break
12            
13            if nums[m] < nums[r]:
14                r = m
15            else:
16                l = m + 1
17            res = min(res, nums[l])
18        
19        return res