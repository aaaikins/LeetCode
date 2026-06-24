# Last updated: 6/24/2026, 2:49:54 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        indexMap = {}
4
5        for i, n in enumerate(nums):
6            diff = target - n
7            if diff in indexMap:
8                return [indexMap[diff], i]
9            indexMap[n] = i