class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0 
        prev = prices[0]
        profit = 0
        first = True

        for i in range(1, len(prices)):
            if(prices[i] <= prev ):
                prev = prices[i]
                continue
            elif (prices[i] > prev):
                profit += prices[i] - prev
                prev = prices[i]
                first = False
            
        return profit
            
        