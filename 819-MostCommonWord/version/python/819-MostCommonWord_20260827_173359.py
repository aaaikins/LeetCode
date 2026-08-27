# Last updated: 8/27/2026, 5:33:59 PM
1class Solution:
2    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
3        freq = defaultdict(int)
4
5        l = 0
6        r = 0
7
8        while r < len(paragraph):
9            if not paragraph[r].isalpha():
10                r += 1
11                l = r
12                continue
13                # break
14            while r < len(paragraph) and paragraph[r].isalpha():
15                r += 1
16
17
18            char = paragraph[l:r].lower()
19
20            if char not in banned:
21                freq[char] += 1 
22
23            l = r
24
25        print(freq)
26        maxk = None
27        maxV = float('-inf')
28        for key,value in freq.items():
29            if value > maxV:
30                maxk = key
31                maxV = value
32
33        return maxk