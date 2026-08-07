class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0 #target itself

        for i in range(n - 2, -1, -1):
            end = min(n, 1 + nums[i] + i)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]