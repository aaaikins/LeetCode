class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums, target, searchLeft=False):
            l, r = 0, len(nums)-1
            idx = -1
            

            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    idx = m
                    if not searchLeft:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return idx

        # def findLast(nums, target):
        #     l, r = 0, len(nums)-1
        #     last = -1

        #     while l <= r:
        #         m = (l+r)//2
        #         if nums[m] == target:
        #             last = m
        #             l = m + 1
        #         elif nums[m] < target:
        #             l = m + 1
        #         else:
        #             r = m - 1
        #     return last

        first = binSearch(nums, target)
        last = binSearch(nums, target, True)
        return [first, last]

        