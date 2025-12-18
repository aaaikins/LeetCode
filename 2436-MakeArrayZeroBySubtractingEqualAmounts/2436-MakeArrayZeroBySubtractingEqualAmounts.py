# Last updated: 12/18/2025, 1:50:25 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        hashSet = set()

        for num in nums:
            if num == 0 or num in hashSet:
                continue
            else:
                hashSet.add(num)

        return len(hashSet)
        