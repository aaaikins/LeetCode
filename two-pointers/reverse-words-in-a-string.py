class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        s = [char.strip() for char in s if char.isalnum()]
        left = 0
        right = len(s) - 1
        print(s)

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return " ".join(s)
        