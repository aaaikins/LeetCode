# Last updated: 12/28/2025, 11:30:34 AM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        # temp = digits[-1] + 1
4
5
6        # i = len(digits) - 1
7        # digits[i] += 1
8        # while i > 0:
9        #     if digits[i] >= 10:
10        #         digits[i - 1] = temp// 10
11        #         digits.append(temp % 10)
12        #     else:
13        #         digits[-1] = temp
14        digits.reverse()
15        digits.append(0)
16        digits[0] += 1
17        # print(digits)
18        i = 0
19        while i < len(digits):
20            if digits[i] >= 10:
21                temp = digits[i]
22                digits[i] = temp % 10
23                digits[i + 1] += (temp // 10)
24            i += 1
25        # print(digits)
26        if digits[-1] == 0:
27            digits.pop()
28        digits.reverse()
29        
30
31
32        return digits 