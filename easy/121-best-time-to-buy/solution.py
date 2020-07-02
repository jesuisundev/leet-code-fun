class Solution(object):
    def maxProfit(self, prices):
        """
        track only the min price and update it
        else update maxprofit
        """
        max_profit = 0
        min_price = None

        for price in prices:
            if min_price is None or price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price


        return max_profit


print(Solution().maxProfit([1,5,3,6,4]))
