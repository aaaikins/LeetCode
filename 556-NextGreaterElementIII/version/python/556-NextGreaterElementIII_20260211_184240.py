# Last updated: 2/11/2026, 6:42:40 PM
1class Solution:
2    def nextGreaterElement(self, n: int) -> int:
3        digits = list(str(n))
4        length = len(digits)
5
6        # Step 1: Find pivot
7        i = length - 2
8        while i >= 0 and digits[i] >= digits[i + 1]:
9            i -= 1
10
11        if i < 0:
12            return -1
13
14        # Step 2: Find rightmost greater digit
15        j = length - 1
16        while digits[j] <= digits[i]:
17            j -= 1
18
19        # Step 3: Swap
20        digits[i], digits[j] = digits[j], digits[i]
21
22        # Step 4: Reverse suffix
23        digits[i + 1:] = reversed(digits[i + 1:])
24
25        result = int("".join(digits))
26
27        # Step 5: Check 32-bit overflow
28        return result if result < 2**31 else -1
29