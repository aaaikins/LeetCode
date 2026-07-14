# Last updated: 7/14/2026, 7:13:04 PM
1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        seen = set()
4        res = []
5
6        for num in nums:
7            if num in seen:
8                res.append(num)
9            seen.add(num)
10        
11        return res
12
13        