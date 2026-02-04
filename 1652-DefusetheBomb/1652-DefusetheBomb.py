# Last updated: 2/4/2026, 6:40:05 PM
1class Solution:
2    def decrypt(self, code: List[int], k: int) -> List[int]:
3        n = len(code)
4        res = [0] * n
5        code = code * n
6        if k == 0:
7            return res
8        
9        elif k > 0:
10            for i in range(n):
11                res[i] = sum(code[i+1: i+ 1 + k])
12        else:
13            for i in range(n):
14                res[i] = sum(code[i+k+n: i+n])
15        
16        return res
17
18
19