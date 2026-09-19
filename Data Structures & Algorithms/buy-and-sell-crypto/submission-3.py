class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minProf = 0
        curBuy = prices[0]

        for sell in prices:
            minProf = max(minProf, sell - curBuy)
            curBuy = min(curBuy, sell)
        return minProf