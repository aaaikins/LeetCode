# Last updated: 12/28/2025, 12:55:43 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def next_num(num):
4            return sum(int(d) ** 2 for d in str(num))
5
6        seen = set()
7
8        while n != 1:
9            n = next_num(n)
10
11            if n in seen:
12                return False
13
14            seen.add(n)
15        
16        return True