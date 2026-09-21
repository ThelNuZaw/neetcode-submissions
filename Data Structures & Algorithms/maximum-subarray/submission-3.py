class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        maxsum = sum(nums)

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxsum = max(maxsum, cursum)
        return maxsum