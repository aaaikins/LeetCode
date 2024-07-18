class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        map_list = []
        for key, val in hashmap.items():
            heappush(map_list, (-val, key))
        
    
        result = []
        while k > 0:
            value, key = heappop(map_list)
            # print(key)
            result.append(key)
            print(k)
            k -= 1

        return result




        


        