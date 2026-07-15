# Last updated: 7/15/2026, 4:09:49 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5
6        for i in range(len(nums)):
7            if nums[i] > 0:
8                break
9
10            if i > 0 and nums[i] == nums[i - 1]:
11                continue
12
13            j, k = i + 1, len(nums) - 1
14
15            while j < k:
16                total = nums[i] + nums[j] + nums[k]
17
18                if total < 0:
19                    j += 1
20                elif total > 0:
21                    k -= 1
22                else:
23                    res.append([nums[i], nums[j], nums[k]])
24                    j += 1
25                    k -= 1
26                    while j < k and nums[j - 1] == nums[j]:
27                        j += 1
28
29        return res