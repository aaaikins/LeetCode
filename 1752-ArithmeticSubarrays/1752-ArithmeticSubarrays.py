# Last updated: 12/18/2025, 1:50:41 PM
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        n = len(r)
        res = []

        for i in range(min(m, n)):
            sub = nums[l[i]: r[i] + 1]
            sub.sort()

            diff = sub[1] - sub[0]
            is_arithmetic = True

            for j in range(2, len(sub)):
                if sub[j] - sub[j - 1] != diff:
                    is_arithmetic = False
            res.append(is_arithmetic)
        
        return res