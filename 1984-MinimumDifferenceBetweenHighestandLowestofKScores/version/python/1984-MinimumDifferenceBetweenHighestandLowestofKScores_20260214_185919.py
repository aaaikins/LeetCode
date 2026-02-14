# Last updated: 2/14/2026, 6:59:19 PM
1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        if len(nums) < 2:
4            return 0
5
6        minDiff = float("inf")
7        nums.sort()
8
9        for i in range(len(nums) -k + 1):
10            diff = nums[i + k - 1] - nums[i]
11            minDiff = min(minDiff, diff)
12
13        return minDiff
14