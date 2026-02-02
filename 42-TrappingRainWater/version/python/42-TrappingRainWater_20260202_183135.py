# Last updated: 2/2/2026, 6:31:35 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l, r = 0, len(height) - 1
4        leftMax, rightMax = height[l], height[r]
5
6        res = 0
7
8        while l < r:
9            if leftMax < rightMax:
10                l += 1
11                leftMax = max(leftMax, height[l])
12                res += leftMax - height[l]
13            
14            else:
15                r -= 1
16                rightMax = max(rightMax, height[r])
17                res += rightMax - height[r]
18            print(leftMax)
19            print(rightMax)
20        return res