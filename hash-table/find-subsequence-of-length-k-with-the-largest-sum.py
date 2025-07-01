class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [-num for num in nums]
        heapify(heap)
        res = [0] * k

        for i in range(k - 1, -1, -1):
            # print(i)
            res[i]= - heappop(heap)


        return res