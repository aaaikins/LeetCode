# Last updated: 7/16/2026, 4:56:59 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        hashmap = {}
4        l = 0
5        longest = 0
6        maxFreq = 0
7
8        for r in range(len(s)):
9            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
10            maxFreq = max(maxFreq, hashmap[s[r]])
11
12            while (r - l + 1) - maxFreq > k:
13                hashmap[s[l]] -= 1
14                l += 1
15            
16            longest = max(longest, r - l + 1)
17
18
19
20        return longest