class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-n, i) for i, n in enumerate(nums)]
        heapify(heap)
        temp = [""] * len(nums)

        for _ in range(k):
            num, idx = heappop(heap)
            temp[idx] = -num
        # print(temp)

        res = []
        for i in range(len(nums)):
            if temp[i] != "":
                res.append(temp[i])

        return res