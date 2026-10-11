class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        sortedNums = sorted(set(nums))
        currentCount = 1
        maxCount = 1

        for i in range(len(sortedNums) - 1):
            currentNum = sortedNums[i]
            nextNum = sortedNums[i + 1]
            if nextNum == currentNum + 1:
                currentCount += 1
            else:
                maxCount = max(maxCount, currentCount)
                currentCount = 1

        return max(maxCount, currentCount)
        
        


        