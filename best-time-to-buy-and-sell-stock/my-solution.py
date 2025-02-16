class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = 10001
        max_profit = 0

        for price in prices:    
            if price < lowest_price:
                lowest_price = price
            profit = price - lowest_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

        Time Complexity: O(n)
        Space Complexity: O(1)
