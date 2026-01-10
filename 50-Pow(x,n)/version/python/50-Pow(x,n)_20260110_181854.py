# Last updated: 1/10/2026, 6:18:54 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        def helper(x, n):
4            if n == 0:
5                return 1
6            half = helper(x, n//2)
7            if n % 2 == 0:
8                return half * half
9            else:
10                return x * half * half
11
12        if n < 0:
13            n = -n
14            x = 1/x
15
16
17        return helper(x, n) 