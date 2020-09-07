class Solution(object):
    def maxProfit(self, prices):
        """
        peak and valley, greedy to study
        https://assets.leetcode.com/static_assets/media/original_images/122_maxprofit_1.PNG
        A + B > C
        """
        current_index = 0
        current_valley = prices[0]
        current_peak = prices[0]
        max_profit = 0

        while current_index < len(prices) - 1:
            # while its going down we didnt reach the valley
            while current_index < len(prices) - 1 and prices[current_index] >= prices[current_index + 1]:
                current_index += 1
            # we reach a valley, we need to keep the value
            current_valley = prices[current_index]

            # while its going up we didnt reach the peak
            while current_index < len(prices) - 1 and prices[current_index] <= prices[current_index + 1]:
                current_index += 1
            # we reach a peak, we need to keep the value
            current_peak = prices[current_index]

            max_profit += current_peak - current_valley

        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))