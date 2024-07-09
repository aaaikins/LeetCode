class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = {}
        for j in range(len(nums)):
            num = nums[j]
            if num in hashmap and abs(hashmap[num] - j) <= k:
                return True
            hashmap[num] = j
        return False
        