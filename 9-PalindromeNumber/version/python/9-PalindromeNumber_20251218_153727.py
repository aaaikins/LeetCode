# Last updated: 12/18/2025, 3:37:27 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5        def reverse(num):
6            rev = 0
7
8            while num > 0:
9                rev = (num % 10) + (rev * 10)
10                num //= 10
11            
12            return rev
13
14        return reverse(x) == x