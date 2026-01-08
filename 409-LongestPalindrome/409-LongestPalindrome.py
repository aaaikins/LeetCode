# Last updated: 1/8/2026, 12:06:02 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        if len(s) == 1:
4            return 1
5
6        count = Counter(s)
7        res = 0
8        has_odd = False
9
10        for ch in count:
11            if count[ch] % 2 == 0:
12                res += count[ch]
13            else:
14                res += count[ch] - 1
15                has_odd = True
16        
17        if has_odd:
18            res += 1
19        
20        return res 
21
22        