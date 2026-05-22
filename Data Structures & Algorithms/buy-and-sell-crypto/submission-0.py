class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mprofit = 0 
        buy = prices[0]
        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                profit = sell - buy
                mprofit = max(profit, mprofit)
        return mprofit
