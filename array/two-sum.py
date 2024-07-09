class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            x = nums[i]
            diff = target - x
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[x] = i
                

        