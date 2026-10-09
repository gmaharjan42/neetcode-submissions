class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))
        currentCount = 1
        maxCount = 1

        if len(sortedNums) == 0:
            return 0
        
        if len(sortedNums) == 1:
            return 1

        for index in range(len(sortedNums) - 1):
            currentNum = sortedNums[index]
            nextNum = sortedNums[index + 1]

            if nextNum == currentNum + 1:
                currentCount += 1
            else:
                maxCount = max(maxCount, currentCount)
                currentCount = 1
        
        return max(maxCount, currentCount)
    