class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start + end)//2
            res = min(res, nums[mid])

            if nums[end] < nums[mid]:
                start = mid + 1
                res = min(res, nums[start])
            else:
                end = mid - 1
                res = min(res, nums[end])

        return res
        