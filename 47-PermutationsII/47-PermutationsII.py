# Last updated: 10/4/2026, 7:46:07 PM
1class Solution:
2    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        result = []
5
6        def backtrack(idx):
7            if idx == len(nums):
8                result.append(nums[:])
9                return
10            
11            used = set()
12            for i in range(idx, len(nums)):
13                
14                if nums[i] in used:
15                    continue
16
17                used.add(nums[i])
18
19                nums[idx], nums[i] = nums[i], nums[idx]
20                backtrack(idx + 1)
21                nums[idx], nums[i] = nums[i], nums[idx]
22
23        backtrack(0)
24        return result
25