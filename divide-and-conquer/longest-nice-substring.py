class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        t = s.lower()
        print(t)

        l = 0
        res = ""
        for r in range(len(t)-1):
            while t[l] != t[r]:
                l += 1
            if r - l + 1 > len(res):
                res = s[l: r + 1]
        
        return res