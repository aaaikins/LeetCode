# Last updated: 12/28/2025, 1:07:59 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n == 0:
4            return 1
5        
6        if n < 0:
7            n = -n
8            x = 1/x
9        
10        if n % 2 == 0:
11            return x**(n/2) * x**(n/2)
12        else:
13            return x * x**(n//2) * x**(n//2)
14        
15        