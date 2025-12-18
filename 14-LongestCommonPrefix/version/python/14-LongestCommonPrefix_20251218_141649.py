# Last updated: 12/18/2025, 2:16:49 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3
4        prefix = strs[0]
5
6        for s in strs[1:]:
7            while not s.startswith(prefix):
8                prefix = prefix[:-1]
9            
10        return prefix
11