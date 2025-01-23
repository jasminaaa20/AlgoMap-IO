class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        buying_price = float('inf')
        max_profit = 0

        for i in range(n):
            if prices[i] < buying_price:
                buying_price = prices[i]
            
            profit = prices[i] - buying_price
            if profit > max_profit:
                max_profit = profit
            
        return max_profit
