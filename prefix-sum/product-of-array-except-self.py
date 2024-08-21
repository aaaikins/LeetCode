class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def helper(nums, num):
            product = 1
            for i in range(len(nums)):
                if nums[i] == num:
                    continue
                product *= nums[i]
            
            return product

        products = []
        for num in nums:
            products.append(helper(nums, num))
        
        return products

                
        