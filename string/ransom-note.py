class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for char in list(magazine):
            magazine_count[char] = magazine_count.get(char, 0) + 1


        for char in ransomNote:
            if char in magazine_count and magazine_count[char] > 0:
                magazine_count[char] -= 1
            else:
                return False
    
        return True