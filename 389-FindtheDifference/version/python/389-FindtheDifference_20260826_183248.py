# Last updated: 8/26/2026, 6:32:48 PM
1class Solution:
2    def compress(self, chars: List[str]) -> int:        
3        l, r = 0, 0
4
5        while r < len(chars):
6            char = chars[r]
7            cnt = 0
8            while r < len(chars) and chars[r] == char:
9                r += 1
10                cnt += 1
11
12            chars[l] = char
13            l += 1
14
15            if cnt > 1:
16                for n in str(cnt):
17                    chars[l] = n
18                    l += 1
19
20        return l