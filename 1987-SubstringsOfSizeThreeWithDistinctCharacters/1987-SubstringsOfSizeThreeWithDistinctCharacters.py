# Last updated: 12/18/2025, 1:50:38 PM
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l= 0
        r=3
        count = 0


        while r < len(s) + 1:
            substring = s[l:r]
            if len(substring) == len(set(substring)):
                count += 1
            l += 1
            r += 1

        return count 
                


        