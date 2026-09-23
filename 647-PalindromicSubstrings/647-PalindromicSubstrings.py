# Last updated: 9/23/2026, 7:46:55 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        
4        def countPalindrome(s, l, r):
5            res = 0
6            while l >= 0 and r < len(s) and s[l] == s[r]:
7                res += 1
8                l -= 1
9                r += 1
10            return res
11        
12        res = 0
13        n = len(s)
14        for i in range(n):
15            res += countPalindrome(s, i, i)
16            res += countPalindrome(s, i, i + 1)
17        
18        return res
19