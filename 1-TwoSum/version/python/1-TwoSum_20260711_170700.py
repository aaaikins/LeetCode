# Last updated: 7/11/2026, 5:07:00 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4
5        for i, n in enumerate(nums):
6            diff = target - n
7            if diff in seen:
8                return [seen[diff], i]
9            seen[n] = i