# Last updated: 2/18/2026, 9:41:28 PM
1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        m, n = len(num1), len(num2)
4        pos = [0] * (m + n)
5
6        for i in range(m -1, -1 , -1):
7            for j in range(n -1, -1, -1):
8                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
9                p1, p2 = i + j, i + j + 1
10                
11                total = product + pos[p2]
12                pos[p2] = total % 10
13                pos[p1] += total // 10
14                
15        
16        res = ''.join(str(d) for d in pos).lstrip('0')
17
18        return res if res != "" else "0"