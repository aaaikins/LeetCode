class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = [char for char in s.split(" ") if char.isalnum()]
        return len(s[-1])
        