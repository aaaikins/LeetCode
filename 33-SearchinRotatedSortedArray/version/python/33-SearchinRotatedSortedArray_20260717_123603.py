# Last updated: 7/17/2026, 12:36:03 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = (l + r) // 2
7
8            if nums[m] == target:
9                return m
10
11            if nums[l] <= nums[m]:
12                if nums[l] <= target < nums[m]:
13                    r = m - 1
14                else:
15                    l = m + 1
16            else:
17                if nums[m] < target <= nums[r]:
18                    l = m + 1
19                else:
20                    r = m - 1
21        
22        return -1