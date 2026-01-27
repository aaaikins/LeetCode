# Last updated: 1/27/2026, 6:54:47 PM
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3        nums = list(set(nums))
4        nums.sort(reverse=True)
5        if len(nums) < 3:
6            return max(nums)
7        return nums[2]