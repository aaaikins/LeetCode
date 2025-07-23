class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        count = 0

        while count < 2:
            for i, num in enumerate(nums):
                # i = i % (len(nums))
                while stack and num > stack[-1][1]:
                    idx, prev = stack.pop()
                    res[idx] = num
                print(i)
                stack.append((i,num))
            count += 1

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
        
        