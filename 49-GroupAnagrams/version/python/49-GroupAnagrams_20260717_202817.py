# Last updated: 7/17/2026, 8:28:17 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        anagramMap = defaultdict(list)
4
5        for s in strs:
6            sorted_s = sorted(s)
7            anagramMap[tuple(sorted_s)].append(s)
8        
9        return list(anagramMap.values())