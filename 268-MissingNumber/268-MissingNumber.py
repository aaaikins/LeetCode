# Last updated: 6/30/2026, 10:47:21 AM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        cur_sum = sum(nums)
4        actual_sum = sum([i for i in range(len(nums)+1)])
5
6        return actual_sum - cur_sum
7        