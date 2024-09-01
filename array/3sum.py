class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            i = l 
            l += 1
            temp = -nums[i]
            if nums[l] == nums[i] and l+1 < r:
                l+=1
            else:
                temp_sum = nums[l] + nums[r]
                if temp_sum < temp:
                    l += 1
                elif temp_sum > temp:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1


        return res
        