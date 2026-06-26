class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_val = prices[0]

        profit = 0 

        for price in prices:

            if price < min_val:

                min_val = price

            elif price - min_val > profit:

                profit = price - min_val

        return profit



