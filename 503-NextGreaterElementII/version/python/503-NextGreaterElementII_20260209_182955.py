# Last updated: 2/9/2026, 6:29:55 PM
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        res = [-1] * n
5        nums = nums * 2
6        stack = []
7        
8        for i, num in enumerate(nums):
9            while stack and num > stack[-1][1]:
10                idx_top, num_top = stack.pop()
11                res[idx_top % n] = num
12            
13            stack.append((i, num))
14
15        return res