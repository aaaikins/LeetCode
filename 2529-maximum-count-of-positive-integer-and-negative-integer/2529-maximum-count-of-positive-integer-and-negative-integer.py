class Solution:
    def find_neg(self, nums):
        l, r = 0, len(nums) - 1
        index = len(nums)

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
                index = mid
        
        return index

    def find_pos(self, nums):
        l, r = 0, len(nums) - 1
        index = len(nums)

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1
                index = mid
        
        return index


    def maximumCount(self, nums: List[int]) -> int:
        # first_non_neg = bisect.bisect_left(nums, 0)
        # first_pos = bisect.bisect_right(nums, 0)
        
        neg = self.find_neg(nums)
        pos = len(nums) - self.find_pos(nums)
        
        return max(neg, pos)

        