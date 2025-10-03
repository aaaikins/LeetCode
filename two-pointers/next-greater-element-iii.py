class Solution:
    def nextGreaterElement(self, n: int) -> int:
        new_n = sorted(str(n), reverse=True)
        new_n = "".join(new_n)
        new_n = int(new_n)
        
        return new_n if new_n > n else -1
        # return 
        