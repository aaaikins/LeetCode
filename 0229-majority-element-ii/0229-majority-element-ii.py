class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # candidate = 0
        # count = 0
        # res = set()

        # for n in nums:
        #     if count == 0:
        #         candidate = n
        #     elif candidate != n:
        #         count -= 1
        #     else:
        #         count += 1
        
        # return list(res)
        n = len(nums)
        count = Counter(nums)
        print(count)
        res = [num for (num, cnt) in count.items() if cnt > (n/3)]

        return res