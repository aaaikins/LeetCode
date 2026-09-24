# Last updated: 9/24/2026, 6:35:42 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        def getPalindrome(s, l, r):
4            while l >= 0 and r < len(s) and s[l] == s[r]:
5                l -= 1
6                r += 1
7            return l, r  # l, r are now one step OUTSIDE the palindrome
8
9        res = ""
10        maxLen = 0
11        l, r = 0, -1  # empty range as default
12
13        for i in range(len(s)):
14            lo, ro = getPalindrome(s, i, i)
15            if (ro - lo - 1) > maxLen:
16                maxLen = ro - lo - 1
17                l, r = lo + 1, ro - 1
18
19            le, re = getPalindrome(s, i, i + 1)
20            if (re - le - 1) > maxLen:
21                maxLen = re - le - 1
22                l, r = le + 1, re - 1
23
24        return s[l: r + 1]