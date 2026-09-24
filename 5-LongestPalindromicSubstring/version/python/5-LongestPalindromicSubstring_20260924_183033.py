# Last updated: 9/24/2026, 6:30:33 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        def getPalindrome(s, l, r):
4            while l >= 0 and r < len(s) and s[l] == s[r]:
5                l -= 1
6                r += 1
7
8            return l, r
9        
10        res = ""
11        maxLen = float("-inf")
12        l, r = 0, 0
13
14        for i in range(len(s)):
15            lo, ro = getPalindrome(s, i, i)
16            if (ro -lo + 1) > maxLen:
17                maxLen = (ro -lo + 1)
18                l, r= lo, ro
19            
20            le, re = getPalindrome(s, i, i + 1)
21            if (re -le + 1) > maxLen:
22                maxLen = (re -le + 1)
23                l, r= le, re
24
25           
26        
27        return s[l+ 1: r]
28