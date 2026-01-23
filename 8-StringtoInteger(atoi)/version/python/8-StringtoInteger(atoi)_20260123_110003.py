# Last updated: 1/23/2026, 11:00:03 AM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        s = s.strip()
4
5        if not s:
6            return 0
7            
8        isNeg = False
9
10        if s[0] == "-":
11            isNeg = True
12            s = s[1:]
13            if not s:
14                return 0
15        elif s[0] == '+':
16            s = s[1:]
17            if not s:
18                return 0
19
20        if not s[0].isdigit():
21            return 0
22
23        num = ""
24        for i in range(len(s)):
25            if not s[i].isdigit():
26                break
27            num += s[i]
28        
29        if isNeg:
30            num = -int(num)
31            if num < -2 ** 31:
32                num = -2 ** 31
33        else:
34            num = int(num)
35            if num > (2**31 - 1):
36                num = 2 ** 31 - 1
37        
38        return num