class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        mapPattern = {}
        mapS = {}
        
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            c1 = pattern[i]
            c2 = s[i]

            if (c1 in mapPattern and mapPattern[c1] != c2) or c2 in mapS and mapS[c2] != c1:
                return False
            mapPattern[c1] = c2
            mapS[c2] = c1
        
        return True