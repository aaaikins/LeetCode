class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        even = []
        odd = []

        for i in num_str:
            i = int(i)
            if i %2 == 0:
                heappush(even, -i)
            else: 
                heappush(odd, -i)
        
        res = ""
        for j in num_str:
            j = int(j)
            if j %2 == 0:
                res += str(-heappop(even))
            else: 
                res += str(-heappop(odd))
        return int(res)