# Last updated: 6/23/2026, 3:56:05 PM
1class Solution:
2    def minOperations(self, n: int) -> int:
3        count = 0
4
5        while n > 0:
6            lower = n - 2**(int(log2(n)))
7            upper = 2**(int(log2(n)) + 1) - n
8
9            n = min(lower, upper)
10            count += 1
11        
12        return count
13