# Last updated: 7/10/2026, 5:42:36 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numSet = set(nums)
4        maxLen = 0
5
6        for num in numSet:
7            if num - 1 not in numSet:
8                cur = 1
9                while num + cur in numSet:
10                    cur += 1
11                maxLen = max(cur, maxLen)
12
13        return maxLen
14
15        