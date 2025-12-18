# Last updated: 12/18/2025, 2:22:06 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        a = 1
4        b = 2
5
6        if n == 1:
7            return 1
8        # if n == 2:
9
10
11        for i in range(n - 2):
12            a, b = b, a + b
13        
14        return b