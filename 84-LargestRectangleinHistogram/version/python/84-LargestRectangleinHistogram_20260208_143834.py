# Last updated: 2/8/2026, 2:38:34 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        maxArea = 0
5
6        for i, h in enumerate(heights):
7            start = i
8
9            while stack and stack[-1][1] > h:
10                idx, height = stack.pop()
11                area = height * (i - idx)
12                maxArea = max(area, maxArea)
13                start = idx
14
15            stack.append((start, h))
16        
17        for i, h in stack:
18            area = h * (len(heights) - i)
19            maxArea = max(maxArea, area)
20
21        return maxArea