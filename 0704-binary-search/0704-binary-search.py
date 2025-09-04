class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def bSearch(nums, target, left, right):
            if left > right:
                return -1

            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bSearch(nums, target, mid + 1, right)
            else:
                return bSearch(nums, target, left, mid - 1)
        
        
        return bSearch(nums, target, l, r)
        