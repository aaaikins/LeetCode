class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [[-s, i] for i, s in enumerate(score)]
        heapify(heap)
        n = len(score)

        res = [0] * n

        for i in range(1, n + 1):
            scr, idx = heappop(heap)
            if i == 1:
                res[idx] = "Gold Medal"
            elif i == 2:
                res[idx] = "Silver Medal"
            elif i == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i)

        return res
        