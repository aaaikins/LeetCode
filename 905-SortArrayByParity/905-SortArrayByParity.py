# Last updated: 10/13/2026, 8:01:21 PM
1class Solution:
2    def sortArrayByParity(self, nums: list[int]) -> list[int]:
3        
4        i = 0
5        j = len(nums) - 1
6
7        while i < j:
8            if nums[i] % 2 == 0:
9                i += 1
10            elif nums[j] % 2 == 1:
11                j -= 1
12            else:
13                nums[i], nums[j] = nums[j], nums[i]
14                i += 1
15                j -= 1
16
17        return nums