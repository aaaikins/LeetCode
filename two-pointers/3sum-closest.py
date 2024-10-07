class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # res = []
        for i, a in enumerate(nums):
            # if a > 0:
            #     break
            # if i > 0 and nums[i-1] == a:
            #     continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < nums[target]:
                    l += 1
                elif threeSum > nums[target]:
                    r -= 1
                else:
                    return threeSum

        # return res
        