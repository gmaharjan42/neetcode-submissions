class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        trappedWater = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    currentWater = leftMax - height[left]
                    trappedWater += currentWater

            else:
                right -= 1

                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    currentWater = rightMax - height[right]
                    trappedWater += currentWater
        
        return trappedWater
            