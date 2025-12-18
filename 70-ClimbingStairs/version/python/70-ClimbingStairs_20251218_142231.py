# Last updated: 12/18/2025, 2:22:31 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        a = 1
4        b = 2
5
6        if n <= 2:
7            return n
8
9        for i in range(n - 2):
10            a, b = b, a + b
11        
12        return b