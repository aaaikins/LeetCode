class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        def happy_function(num): 
            total = 0
            for c in str(num):
                total += int(c) ** 2
            return total

        res = n
        while res != 1: 
            res = happy_function(res)
            if res in visited:
                return False
            visited.add(res)

        return True



# class Solution:
#     def isHappy(self, n: int) -> bool:
#         num = str(n)
#         total = 0
#         i = 0
#         while len(num) > 1:
#             total += int(num[i]) ** 2
#             i += 1
#             if i == len(num):
#                 num = str(total)
#                 i = 0

#         if int(num) == 1:
#             return True
#         else:
#             return False
        

        