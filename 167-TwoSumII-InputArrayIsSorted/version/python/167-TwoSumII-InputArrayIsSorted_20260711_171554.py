# Last updated: 7/11/2026, 5:15:54 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        l, r = 0, len(nums) - 1
4
5        while l < r:
6            total = nums[l] + nums[r]
7
8            if total < target:
9                l += 1
10            elif total > target:
11                r -=1
12            else:
13                return [l + 1, r + 1]