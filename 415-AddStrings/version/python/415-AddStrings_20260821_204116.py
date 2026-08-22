# Last updated: 8/21/2026, 8:41:16 PM
1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        num1, num2 = list(num1), list(num2)
4        i, j = len(num1) - 1, len(num2) - 1
5
6        res = ""  
7        carry = 0
8        
9        while i >= 0 and j >= 0:
10            int1 = int(num1[i]) if i >= 0 else 0
11            int2 = int(num2[j]) if j >= 0 else 0
12
13            total = int1 + int2 + carry
14            res += str(total % 10)
15            carry = total // 10
16            i -= 1
17            j -= 1
18
19        while i >= 0:
20
21            total = int(num1[i]) + carry
22            res += str(total % 10)
23            carry = total // 10
24            i -= 1
25
26        while j >= 0:
27            total = int(num2[j]) + carry
28            res += str(total % 10)
29            carry = total // 10
30            j -= 1
31
32        if carry:
33            res += str(carry)
34
35        return res[::-1]
36