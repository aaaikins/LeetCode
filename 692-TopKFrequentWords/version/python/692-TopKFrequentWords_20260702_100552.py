# Last updated: 7/2/2026, 10:05:52 AM
1class Solution:
2    def topKFrequent(self, words: List[str], k: int) -> List[str]:
3        count = Counter(words)
4        heap = [(-freq, word) for word, freq in count.items()]
5        heapify(heap)
6        res = []
7
8        while len(res) != k:
9            _, word = heappop(heap)
10            res.append(word)
11        
12        return res