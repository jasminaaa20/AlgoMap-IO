class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')  # Initialize with infinity for better flexibility
        max_profit = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price  # Update the lowest price seen so far
            max_profit = max(max_profit, price - lowest_price)  # Track max profit
        
        return max_profit
        # Time Complexity: O(n)
        # Space Complexity: O(1)
