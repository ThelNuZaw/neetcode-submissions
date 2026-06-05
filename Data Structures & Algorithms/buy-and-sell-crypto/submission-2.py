class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                #make profit
                profit = prices[right] - prices[left]
                maxpro = max(maxpro, profit)
            else:
                left = right
            right += 1
        return maxpro