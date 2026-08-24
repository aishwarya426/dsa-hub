class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            elif prices[i] - min >maxprofit:
                maxprofit=prices[i]-min
                

        return maxprofit

              



        