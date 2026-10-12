# Last updated: 10/12/2026, 7:54:36 PM
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        seen = {}
4
5        for i, num in enumerate(nums):
6            diff = target - num
7            if diff in seen:
8                return [seen[diff], i]
9            else:
10                seen[num] = i
11
12    