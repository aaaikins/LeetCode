class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        start_word = strs[0]

        for i in range(len(start_word)):
            for s in strs:
                if i == len(s) or s[i] != start_word[i]:
                    return prefix
    
            prefix += start_word[i]

        return prefix

        
            

            
        