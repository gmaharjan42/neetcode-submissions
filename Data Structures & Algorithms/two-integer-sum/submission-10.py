class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrayMap = {}

        for index, number in enumerate(nums):
            diff = target - number

            if diff in arrayMap:
                return [arrayMap[diff], index]
            else:
                arrayMap[number] = index
        
        