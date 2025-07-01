class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        even = []
        odd = []
        start = int(num_str[0])
        for i in num_str:
            i = int(i)
            if i %2 == 0:
                heappush(even, -i)
            else: 
                heappush(odd, -i)
        
        res = ""
        for _ in range(len(num_str)//2):
            if start %2 == 0:
                res += str(-heappop(even))
                res += str(-heappop(odd))
            else:
                res += str(-heappop(odd))
                res += str(-heappop(even))

        if len(res) < len(num_str):
            res += num_str[-1]
        return int(res)