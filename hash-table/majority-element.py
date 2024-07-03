class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        for num in hashmap:
            if hashmap.get(num) > n/2:
                return num
        
        