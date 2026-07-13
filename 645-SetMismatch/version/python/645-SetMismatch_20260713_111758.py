# Last updated: 7/13/2026, 11:17:58 AM
1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        seen = set()
4        res = []
5
6        for i, n  in enumerate(nums):
7            if n in seen:
8                res.append(n)
9            seen.add(n)
10        
11        
12        for i in range(1, len(nums) + 1):
13            if i not in seen:
14                res.append(i)
15                break
16        
17        return res
18
19