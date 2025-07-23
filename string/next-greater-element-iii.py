class Solution:
    def nextGreaterElement(self, n: int) -> int:
        new_int = int(str(n)[::-1])

        return new_int if new_int > n else -1
        