# Last updated: 2/4/2026, 6:42:45 PM
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        new_code = code + code + code
        num = len(code)
        res = [0] * len(code)

        for i in range(num):
            if k < 0:
                res[i] = sum(new_code[num+k+i:i+num])
            if k > 0:
                res[i] = sum(new_code[num+i+1:k+num+i+1])
        return res
