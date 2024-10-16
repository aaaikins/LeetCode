class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            
            # If the mid element is the target
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[start] <= nums[mid]:
                # Check if the target is in the left half
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
