class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        [3,2,3]
             n
        num = 0 = 3 
        count = 0 = 1 = 0 = 1
        '''

        num = 0
        count = 0

        for n in nums:
            if count == 0:
                num = n
            elif n != num:
                count -= 1
            else:
                count += 1

        return num
        