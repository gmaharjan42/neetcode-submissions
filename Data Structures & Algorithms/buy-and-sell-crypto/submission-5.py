class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        currentP = 0
        maxP = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                currentP = 0
                l = r
                r += 1
                if currentP > maxP:
                    maxP = currentP
            
            else:
                currentP = prices[r] - prices[l]
                if currentP > maxP:
                    maxP = currentP
                
                r += 1
            
        return maxP