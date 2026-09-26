class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in seen_numbers:
                return [seen_numbers[diff], index]
            else:
                seen_numbers[number] = index 
