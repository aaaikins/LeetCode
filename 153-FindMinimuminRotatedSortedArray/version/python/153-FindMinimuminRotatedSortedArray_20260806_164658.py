# Last updated: 8/6/2026, 4:46:58 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4
5        res = nums[l]
6
7        while l < r:
8            m = (l + r) // 2
9            
10            if nums[m] < nums[r]:
11                r = m
12            else:
13                l = m + 1
14
15            res = min(res, nums[l])
16
17            
18
19        
20        return nums[l]