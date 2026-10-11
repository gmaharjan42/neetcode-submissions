class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = [10203291] + numbers

        seenNumbers = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in seenNumbers:
                return [seenNumbers[difference], index]
            seenNumbers[num] = index
        