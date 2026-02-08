# Last updated: 2/8/2026, 2:52:28 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        res = [0] * len(temperatures)
5        
6        for i, t in enumerate(temperatures):
7
8            while stack and t > stack[-1][1]:
9                idx, temp = stack.pop()
10                res[idx] = i - idx
11                
12            stack.append((i, t))
13
14        return res