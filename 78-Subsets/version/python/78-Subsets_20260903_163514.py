# Last updated: 9/3/2026, 4:35:14 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = [[]]
4
5        for num in nums:
6            res += [subset + [num] for subset in res]
7
8        return res
9        