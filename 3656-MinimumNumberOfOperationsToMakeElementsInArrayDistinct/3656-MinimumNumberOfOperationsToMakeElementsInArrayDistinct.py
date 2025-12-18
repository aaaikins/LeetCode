# Last updated: 12/18/2025, 1:50:00 PM
import math
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        
        # Traverse from end to start
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                break
            seen.add(nums[i])
        else:
            # If the loop completes without breaking, all elements are distinct
            return 0
        
        # Otherwise, need to remove first (i + 1) elements
        return math.ceil((i + 1) / 3)
