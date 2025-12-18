# Last updated: 12/18/2025, 1:50:36 PM
class Solution:
    def isThree(self, n: int) -> bool:
        nDiv = 0

        for i in range(1, n+1):
            if n % i == 0:
                nDiv += 1
            else:
                continue
        print(nDiv)
        return nDiv == 3
        