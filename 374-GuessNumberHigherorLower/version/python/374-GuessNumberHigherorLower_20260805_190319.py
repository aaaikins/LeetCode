# Last updated: 8/5/2026, 7:03:19 PM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        
11
12        l, r = 1, n
13        # pick = guess(n)
14
15        while l <= r:
16            m = (l + r) // 2
17            pick = guess(m)
18            if pick == -1:
19                r = m - 1
20            elif pick == 1:
21                l = m + 1
22            else:
23                return m
24