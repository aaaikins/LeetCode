# Last updated: 12/18/2025, 1:50:45 PM
from collections import Counter, defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)
        window = Counter()
        unique = 0

        # Initialize window
        for i, c in enumerate(s):
            window[c] += 1
            if window[c] == 1:
                unique += 1

            # Remove char if window exceeds minSize
            if i >= minSize:
                left = s[i - minSize]
                window[left] -= 1
                if window[left] == 0:
                    unique -= 1

            # Check valid substring
            if i >= minSize - 1 and unique <= maxLetters:
                sub = s[i - minSize + 1 : i + 1]
                freq[sub] += 1

        return max(freq.values(), default=0)
