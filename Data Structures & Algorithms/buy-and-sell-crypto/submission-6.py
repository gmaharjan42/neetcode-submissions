class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        currentP = 0
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currentP = prices[r] - prices[l]
                if currentP > maxP:  
                    maxP = currentP
                r += 1
            else:
                l = r
                r += 1
                currentP = 0
        
        return maxP

            

        