class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        return max(hashmap.values())
        