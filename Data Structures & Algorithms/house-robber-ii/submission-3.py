class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.houserob(nums[1:]), self.houserob(nums[:len(nums) - 1]))

    def houserob(self, house):
        if not house:
            return 0
        if len(house) == 1:
            return house[0]
        dp = [0] * len(house)
        dp[0] = house[0]
        dp[1] = max(house[0], house[1])

        for h in range(2, len(house)):
            dp[h] = max(house[h] + dp[h - 2], dp[h - 1])
        return dp[len(house) - 1]