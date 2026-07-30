class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = 1
        curMax = 1
        res = max(nums)
        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
            temp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res