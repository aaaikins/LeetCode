# Last updated: 8/21/2026, 8:42:52 PM
1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        i, j = len(num1) - 1, len(num2) - 1
4        carry = 0
5        res = []
6
7        while i >= 0 or j >= 0 or carry:
8            d1 = int(num1[i]) if i >= 0 else 0
9            d2 = int(num2[j]) if j >= 0 else 0
10            total = d1 + d2 + carry
11            res.append(str(total % 10))
12            carry = total // 10
13            i -= 1
14            j -= 1
15
16        return ''.join(reversed(res))