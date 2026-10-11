class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaList = []
        left = 0
        right = len(heights) - 1
        while left < right:
            currentWidth = right - left
            currentHeight = min(heights[left], heights[right])
            currentArea = currentWidth * currentHeight
            areaList.append(currentArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        maxArea = max(areaList)
        return maxArea
    