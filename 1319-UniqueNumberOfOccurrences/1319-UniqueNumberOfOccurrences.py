# Last updated: 12/18/2025, 1:50:47 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for num in arr:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
            
        return len(set(hashmap.values())) == len(hashmap.values())