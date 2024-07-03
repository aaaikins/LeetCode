class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        
        
        nums = []
        for i in range(len(s)):
            nums.append(roman[s[i]])
        
        number = nums[-1]
        
        for i in range(len(s)-1):
            if (nums[i] < nums[i+1]):
                number -= nums[i]
            else:
                number += nums[i]
        
        return number 

        