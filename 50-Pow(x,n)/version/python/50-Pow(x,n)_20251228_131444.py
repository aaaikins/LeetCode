# Last updated: 12/28/2025, 1:14:44 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n == 0:
4            return 1
5        
6        if n < 0:
7            n = -n
8            x = 1/x
9
10        results = 1
11
12        while n > 0:
13            if n % 2 == 1:
14                results *= x
15
16            x *= x
17            n //= 2 
18        
19        return results
20        
21        