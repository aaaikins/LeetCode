class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [[-s, i] for i, s in enumerate(score)]
        heapify(heap)
        n = len(score)

        res = [0] * n
        hashmap = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal"
        }

        for i in range(1, min(n, len(hashmap)) + 1):
            scr, idx = heappop(heap)
            res[idx] = hashmap[str(i)]

        for j in range(4, n + 1):
            scr, idx = heappop(heap)
            res[idx] = str(j)

        # print(heap)

        return res
        