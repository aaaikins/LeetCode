# Last updated: 7/13/2026, 11:24:23 AM
1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        seen = set()
4        res = []
5
6        for n in nums:
7            if n in seen:
8                res.append(n)
9            seen.add(n)
10        
11        for n in range(1, len(nums) + 1):
12            if n not in seen:
13                res.append(n)
14                break
15        
16        return res
17
18