# Last updated: 6/24/2026, 2:36:15 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        
6        count_s = [0] * 26
7        count_t = [0] * 26
8
9        for i in range(len(s)):
10            count_s[ord(s[i]) - ord('a')] += 1
11            count_t[ord(t[i]) - ord('a')] += 1
12        
13        return count_s == count_t