# Last updated: 7/14/2026, 7:34:19 PM
1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        res = []
4
5        for num in nums:
6            idx = abs(num) - 1
7
8            if nums[idx] < 0:
9                res.append(idx + 1)
10            else:
11                nums[idx] *= -1
12        
13        return res