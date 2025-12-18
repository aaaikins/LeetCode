# Last updated: 12/18/2025, 1:50:48 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        res = [0] * n

        for i in range(n - 1, -1, -1):
            count = 0

            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            
            if stack:
                count += 1
                
            stack.append(heights[i])
            res[i] = count
        
        return res

        