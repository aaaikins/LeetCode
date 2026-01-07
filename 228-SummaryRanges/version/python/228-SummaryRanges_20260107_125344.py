# Last updated: 1/7/2026, 12:53:44 PM
1class Solution:
2    def summaryRanges(self, nums: List[int]) -> List[str]:
3        if not nums:
4            return []
5        
6        n = len(nums)
7        res = []
8        i = 0
9        while i < n:
10            a = b = nums[i]
11            while i + 1 < n and nums[i + 1] == nums[i] + 1:
12                b = nums[i + 1]
13                i += 1
14            if a == b:
15                res.append(str(a))
16            else:
17                res.append(f"{a}->{b}")
18            
19            i += 1
20        
21        return res
22            