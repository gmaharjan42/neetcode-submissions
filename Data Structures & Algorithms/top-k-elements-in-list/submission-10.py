class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap, kHeap, answer = {}, [], []

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        for num, freq in freqMap.items():
            heapq.heappush(kHeap, (freq, num))
            if len(kHeap) > k:
                heapq.heappop(kHeap)
        
        for freq, num in kHeap:
            answer.append(num)
        
        return answer