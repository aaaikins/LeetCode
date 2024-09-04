class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start+end) // 2
            
            if nums[mid + 1] < nums[mid]:
                res = min(res, nums[mid + 1])
            
            if nums[mid] < nums[mid - 1]:
                res = min(res, nums[mid])
            
            if nums[end] > nums[mid]:
                end = mid - 1
            else: 
                start = mid + 1
                
        return res

                 

        