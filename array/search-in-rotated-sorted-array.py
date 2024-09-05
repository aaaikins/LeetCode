class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) -1

        while start <= end:
            mid = (start + end)// 2
            if target < nums[mid]:
                if target < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif target > nums[mid]:
                if target < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                return mid

        
        return -1
        