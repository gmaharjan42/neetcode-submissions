class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #i first want to create a hashmap that counts the frequency
        #of each nuber in the array
        countNums = {}

        #i also want to create an empty list where i will later store
        #all of the keys sorted based on their frequency values
        freqList = []

        #this is the for loop for that number frequency counter
        for number in nums:
            if number in countNums:
                countNums[number] += 1
            else:
                countNums[number] = 1

        freqList = sorted(countNums, key = countNums.get, reverse = True)

        freqList = freqList[:k]

        return freqList



        