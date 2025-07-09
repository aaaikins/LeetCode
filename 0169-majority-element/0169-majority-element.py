class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = 0
        count = 0

        for n in nums:
            if count == 0:
                num = n
                count += 1
            elif n != num:
                count -= 1
            else:
                count += 1

        return num
        