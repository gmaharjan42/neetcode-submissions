class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevIntMap = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in prevIntMap:
                return [prevIntMap[diff], index]
            prevIntMap[value] = index
        return