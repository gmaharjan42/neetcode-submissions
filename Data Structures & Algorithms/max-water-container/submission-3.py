class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            currentWidth = right - left
            currentHeight = min(heights[left],heights[right])
            currentArea = currentWidth * currentHeight
            if currentArea > maxArea:
                maxArea = currentArea

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea