# Last updated: 1/5/2026, 3:25:33 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        def halfPow(x, n):
4            if n == 0:
5                return 1
6            
7            if n < 0:
8                n = -n
9                x = 1/x
10            
11            half = halfPow(x, n//2)
12
13            if n %2 == 0:
14                return half * half
15            else:
16                return x * half * half
17        
18        return halfPow(x, n)
19        
20        