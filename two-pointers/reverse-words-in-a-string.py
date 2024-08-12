class Solution:
    def reverseWords(self, s: str) -> str:
        s = [char for char in s.split(" ") if char.isalnum()]
        left = 0
        right = len(s) - 1
 

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return " ".join(s)
        