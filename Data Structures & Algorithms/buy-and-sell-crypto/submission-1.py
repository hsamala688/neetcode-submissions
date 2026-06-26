class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''

        min_val = prices[0]

        profit = 0 

        for price in prices:

            if price < min_val:

                min_val = price

            elif price - min_val > profit:

                profit = price - min_val

        return profit

        '''

        min_val = prices[0]

        profit = 0 

        for i in range(len(prices)):

            if prices[i] < min_val:

                min_val = prices[i]

            elif prices[i] > min_val:

                new_profit = prices[i] - min_val

                profit = max(new_profit, profit)

        return profit

