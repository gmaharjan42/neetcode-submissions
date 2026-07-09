class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevIndexMap = {}

        for eachIndex, eachValue in enumerate(nums):
            diff = target - eachValue
            if diff in prevIndexMap:
                return [prevIndexMap[diff], eachIndex]
            prevIndexMap[eachValue] = eachIndex
        return