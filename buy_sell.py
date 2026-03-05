class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0

        for i in range(0, len(prices)):
            if prices[i] < min:
                min = prices[i]      

            profit = prices[i] - min 

            if profit > max:
                max = profit    

        return max