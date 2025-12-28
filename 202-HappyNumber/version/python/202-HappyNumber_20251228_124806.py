# Last updated: 12/28/2025, 12:48:06 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def num_to_list(num):
4            return [int(i) for i in str(n)]
5
6        seen = set()
7
8        while n != 1:
9            n = num_to_list(n)
10            accum = 0
11            for i in n:
12                accum += i ** 2
13            if accum in seen:
14                return False
15
16            seen.add(accum)
17            n = accum
18        
19        return True
20            
21
22