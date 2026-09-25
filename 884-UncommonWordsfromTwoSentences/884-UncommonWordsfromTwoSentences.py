# Last updated: 9/25/2026, 7:42:19 PM
1from collections import Counter
2
3class Solution:
4    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
5        count = Counter((s1 + " " + s2).split())
6        return [word for word, c in count.items() if c == 1]