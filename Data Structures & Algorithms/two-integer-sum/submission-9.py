class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for index, number in enumerate(nums):
            difference = target - number

            if difference in seen_numbers:
                return [seen_numbers[difference], index]
            else:
                seen_numbers[number] = index
