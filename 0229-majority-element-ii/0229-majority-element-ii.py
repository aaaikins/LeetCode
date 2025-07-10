class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # candidate = 0
        # count = 0


        # for n in nums:
        #     if count == 0:
        #         candidate = n
        #         count += 1
        #     if candidate != n:
        #         count -= 1
        #     else:
        #         count += 1
        
        # return candidate
        n = len(nums)
        count = Counter(nums)
        res = [num for (num, cnt) in count.items() if cnt > (n//3)]

        return res