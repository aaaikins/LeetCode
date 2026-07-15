# Last updated: 7/15/2026, 2:57:20 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = [c.lower() for c in s if c.isalnum()]
4        print(s)
5        l, r = 0, len(s) - 1
6
7        while l <= r:
8            if s[l] != s[r]:
9                return False
10            
11            l += 1
12            r -= 1
13        
14        return True