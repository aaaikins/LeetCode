# Last updated: 2/8/2026, 2:52:24 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        res = [0] * len(temperatures)
5        
6        for i, t in enumerate(temperatures):
7            while stack and t > stack[-1][1]:
8                idx, temp = stack.pop()
9                res[idx] = i - idx
10            stack.append((i, t))
11
12        return res