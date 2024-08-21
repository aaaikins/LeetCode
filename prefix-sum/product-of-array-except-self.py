class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        iteration = 0 
        res = []
        prod = 1
        while iteration < len(nums):
            for idx, num in enumerate(nums):
                if idx != iteration:
                    prod = prod * num
            
            res.append(prod)
            prod = 1
            iteration +=1
        return res
        