# Last updated: 12/18/2025, 3:19:34 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        goal = len(nums) - 1
4
5        for i in range(len(nums) -1, -1, -1):
6            if i + nums[i] >= goal:
7                goal = i
8        
9        return goal == 0