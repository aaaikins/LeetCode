class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        carry = 0

        while i >= 0 or j >= 0 or carry:
            a1 = int(a[i]) if i >= 0 else 0
            b2 = int(b[j]) if j >= 0 else 0
            total = a1 + b2 + carry

            carry = total // 2
            res += str(total % 2)

            i -= 1
            j -= 1

        return res[::-1]
