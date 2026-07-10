# Last updated: 7/10/2026, 5:37:33 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numsSet = set(nums)
4        res = 0
5
6        for num in numsSet:
7            if num - 1 not in numsSet:
8                cur = 1
9                while (num + cur) in numsSet:
10                    cur += 1
11                res = max(cur, res)
12        
13        return res