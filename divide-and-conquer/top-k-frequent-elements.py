class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        map_list = [(-val, key) for key, val in hashmap.items()]
        heapify(map_list)
        
        result = []
        while k > 0:
            value, key = heappop(map_list)
            result.append(key)
            k -= 1

        return result




        


        