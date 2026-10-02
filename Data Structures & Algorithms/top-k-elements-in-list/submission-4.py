class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numStore = {}
        freqMap = []

        for num in nums:
            if num in numStore:
                numStore[num] += 1
            else:
                numStore[num] = 1

        
        freqMap = sorted(numStore, key = numStore.get, reverse = True)
        freqMap = freqMap[:k]

        return freqMap

        
        
