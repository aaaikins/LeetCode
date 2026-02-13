# Last updated: 2/13/2026, 1:06:15 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        n = len(nums)
4        goal = n - 1
5
6        for i in range(n-1, -1, -1):
7            if nums[i] + i >= goal:
8                goal = i
9
10        return goal == 0