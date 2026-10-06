class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        freqList = []

        for number in nums:
            if number in countNums:
                countNums[number] += 1
            else:
                countNums[number] = 1
        
        freqList = sorted(countNums, key = countNums.get, reverse = True)

        freqList = freqList[:k]

        return freqList