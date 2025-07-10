class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        # countMap = Counter(nums)

        # count = [[num, cnt] for num, cnt in countMap.items() if num % 2 == 0]

        # maxfreq = -inf
        # res = -1
        # for n, c in count:
        #     if c > maxfreq:
        #         maxfreq = c
        #         res = n
        #     elif c == maxfreq:
        #         res = min(res, n)

        # # print(res)
        # return res

        candidate1, candidate2 = -1, -1
        count1, count2 = 0, 0

        for n in nums:
            if n % 2 != 0:
                continue
            else:
                if n == candidate1:
                    count1 += 1
                elif n == candidate2:
                    count2 += 1
                elif count1 == 0:
                    candidate1 = n
                    count1 = 1
                elif count2 == 0:
                    candidate2 = n
                    count2 = 1
                else:
                    count1 -= 1
                    count2 -= 1

        count1 = count2 = 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
        
        if count1 == count2:
            return min(candidate1, candidate2)
        else:
            return max(candidate1, candidate2)