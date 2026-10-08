class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} #empty hashmap to start

        for index, number in enumerate(nums):
            diff = target - number

            if diff in numMap:
                return [numMap[diff], index]
            else:
                #making the key of the hashmap the number and the value the index since we care more about the index here
                numMap[number] = index 
        