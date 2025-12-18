# Last updated: 12/18/2025, 1:50:24 PM
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        countMap = Counter(nums)

        count = [[num, cnt] for num, cnt in countMap.items() if num % 2 == 0]

        maxfreq = -inf
        res = -1
        for n, c in count:
            if c > maxfreq:
                maxfreq = c
                res = n
            elif c == maxfreq:
                res = min(res, n)

        # print(res)
        return res

