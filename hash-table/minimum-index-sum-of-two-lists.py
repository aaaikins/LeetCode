class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        minSum = float('inf')
        res = []


        for i, item in enumerate(list1):
            hashmap[item] = i

        for j, itm in enumerate(list2):
            if itm in hashmap and hashmap[itm] + i <= minSum:
                

                if hashmap[itm] + i < minSum:
                    res.clear()
                    minSum = hashmap[itm] + i
                
                res.append(itm)
                print(res)
        return res
        

        