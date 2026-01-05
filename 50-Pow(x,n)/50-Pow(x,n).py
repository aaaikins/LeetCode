# Last updated: 1/5/2026, 3:23:29 PM
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
11        while n > 0:
12            if n % 2 == 1:
13                results *= x
14            x *= x
15            n //= 2
16        
17        return results 
18
19        """
20        2 ^ 10 = 2^5 * 2^5
21        2 ^ 5 = 2 * 2^2 *2 ^2
22        """
23        
24        