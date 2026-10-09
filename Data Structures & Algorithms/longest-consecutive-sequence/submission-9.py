class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        count = 1

        if len(sortedNums) == 0:
            return 0

        currentCount = 1
        maxCount = 1

        for i in range(len(sortedNums) - 1):
            currentNumber = sortedNums[i]
            nextNumber = sortedNums[i + 1]

            # Ignore duplicate numbers

            if nextNumber == currentNumber:

                continue

            # If consecutive, increase current sequence

            elif nextNumber == currentNumber + 1:

                currentCount += 1

            # Sequence was broken, so start over

            else:

                maxCount = max(maxCount, currentCount)
                currentCount = 1

        # Check one final time in case the longest sequence
        # continued until the end of the list

        maxCount = max(maxCount, currentCount)
        return maxCount
            

        