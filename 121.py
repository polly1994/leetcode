class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
        """
        超过了time limite brute force
        max_profit = 0
        length = len(prices)
        for i in range(length):
            for j in range(i):
                if prices[j] < prices[i] and prices[i]-prices[j]>max_profit:
                    max_profit = prices[i] - prices[j]
                    
        return max_profit
        """
