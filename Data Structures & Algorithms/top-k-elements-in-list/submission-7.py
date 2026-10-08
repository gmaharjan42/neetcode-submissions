class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        freqList = []

        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        
        freqList = sorted(numMap, key = numMap.get, reverse = True)
        freqList = freqList[:k]
        return freqList
        