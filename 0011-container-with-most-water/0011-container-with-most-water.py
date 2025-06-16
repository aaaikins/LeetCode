class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_area = -float("inf")

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            max_area = max(area, max_area)
        
        return max_area

        