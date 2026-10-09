class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_pointer = 0
        sell_pointer = 1
        while sell_pointer < len(prices):
            if prices[sell_pointer] > prices[buy_pointer]:
                current_profit = prices[sell_pointer] - prices[buy_pointer]
                max_profit = max(current_profit, max_profit)
                sell_pointer += 1
            else:
                buy_pointer = sell_pointer
                sell_pointer += 1
        return max_profit