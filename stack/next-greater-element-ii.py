class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                res[idx] = curr
            if i < n:  # Only push index during the first pass
                stack.append(i % n)

        return res



# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         next_greater = {}
#         stack = []

#         for num in nums2:
#             while stack and num > stack[-1]:
#                 prev = stack.pop()
#                 next_greater[prev] = num
#             stack.append(num)

#         return [next_greater.get(num, -1) for num in nums1]
        
        