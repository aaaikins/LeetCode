# Last updated: 8/21/2026, 7:29:01 PM
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        res = []
4
5        for i in range(1, n + 1):
6            if i %3 == 0 and i % 5 == 0:
7                res.append("FizzBuzz")
8            elif i % 3 == 0:
9                res.append("Fizz")
10            elif i % 5 == 0:
11                res.append("Buzz")
12            else:
13                res.append(str(i))
14        
15        return res
16
17        