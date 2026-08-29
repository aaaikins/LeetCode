# Last updated: 8/29/2026, 6:48:42 PM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        res = 0
4        is_neg = (dividend < 0) != (divisor < 0)
5        dividend, divisor = abs(dividend), abs(divisor)
6        
7        while dividend >= divisor:
8            temp = divisor
9            multiple = 1
10            while dividend >= (temp << 1):
11                temp <<= 1
12                multiple <<= 1
13            dividend -= temp
14            res += multiple
15
16        if is_neg:
17            res = -res
18        
19        res = min(max(res, -2**31), 2**31 - 1)
20        return res