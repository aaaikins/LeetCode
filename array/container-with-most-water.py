class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -float('inf')
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[r], height[l]) * (r - l)
            
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                # area = abs(height[r] - height[l]) * (r - l)
                l += 1
                r -= 1

            max_area = max(area, max_area)
        
        return max_area

        