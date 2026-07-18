# Last updated: 7/17/2026, 8:41:04 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        """
4        sorted(s) == sorted(t)
5
6        strs = ["eat","tea","tan","ate","nat","bat"]
7
8        "aet" = "aet"
9
10        anagramMap = {
11            "aet": ["eat", "tea", "ate"]
12            "ant": ["tan", "nat"]
13            "abt": ["bat"]
14        }
15        
16        list(angramMap.values())
17        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
18        """
19
20        anagramMap = {}
21
22        for s in strs:
23            sorted_s = tuple(sorted(s))
24            if sorted_s in anagramMap:
25                anagramMap[sorted_s].append(s)
26            else:
27                anagramMap[sorted_s] = [s]
28        
29        return list(anagramMap.values())