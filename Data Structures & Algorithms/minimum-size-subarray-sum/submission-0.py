class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left = 0
        sumofnums = 0
        for right in range(len(nums)):
            sumofnums += nums[right]

            while sumofnums >= target:
                res = min(res, right - left + 1)
                sumofnums -= nums[left]
                left += 1
        return 0 if res == float("inf") else res