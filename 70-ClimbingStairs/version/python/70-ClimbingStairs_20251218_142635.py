# Last updated: 12/18/2025, 2:26:35 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5
6        a = 1
7        b = 2
8
9        for i in range(3, n + 1):
10            a, b = b, a + b
11        
12        return b