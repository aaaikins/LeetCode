class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        [2,2,1,1,1,2,2]
                     n
        candidate = None => 2 => 1 => 2
        count = 0 => 1 => 2 => 1 => 0 => 1 => 0 => 1

        count = 4 - 3 = 1
        '''

        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
                count = 1
            elif n != candidate:
                count -= 1
            else:
                count += 1
        
        count = 0
        for n in nums:
            if n == candidate:
                count += 1
        
        print(count)
        if count > n/2:
            return candidate
        