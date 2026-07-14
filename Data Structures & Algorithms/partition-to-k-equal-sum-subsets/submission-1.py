class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k

        used = [False] * len(nums)

        def dfs(i, k, sumsub):
            if k == 0:
                return True
            if target == sumsub:
                return dfs(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or sumsub + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j + 1, k, sumsub + nums[j]):
                    return True
                used[j] = False
            return False

        return dfs(0, k, 0)