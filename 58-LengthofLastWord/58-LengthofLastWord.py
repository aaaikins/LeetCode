# Last updated: 1/5/2026, 4:56:48 PM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s = s.strip().split(" ")
4        return len(s[-1])