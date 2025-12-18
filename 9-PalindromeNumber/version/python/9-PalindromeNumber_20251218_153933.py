# Last updated: 12/18/2025, 3:39:33 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5
6        original = x
7        rev = 0
8
9        while x > 0:
10            rev = rev * 10 + x % 10
11            x //= 10
12
13        return rev == original
14