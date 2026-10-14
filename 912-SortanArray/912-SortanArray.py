# Last updated: 10/14/2026, 3:24:05 PM
1class Solution:
2    def sortArray(self, nums: list[int]) -> list[int]:
3        def merge(l1, l2, result):
4            i1, i2 = 0, 0
5
6            while i1 < len(l1) and i2 < len(l2):
7                if l1[i1] < l2[i2]:
8                    result.append(l1[i1])
9                    i1 += 1
10                else:
11                    result.append(l2[i2])
12                    i2 += 1
13            
14            if i1 < len(l1):
15                result.extend(l1[i1:])
16
17            if i2 < len(l2):
18                result.extend(l2[i2:])
19
20            return result
21
22
23        n = len(nums)
24
25        if n <= 1:
26            return nums
27        
28        l = self.sortArray(nums[:n//2])
29        r = self.sortArray(nums[n//2:])
30
31        return merge(l, r, [])
32        
33        
34