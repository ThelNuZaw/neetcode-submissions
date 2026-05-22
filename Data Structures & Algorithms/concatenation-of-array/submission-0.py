class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(len(nums)):
            ans[i] = nums[i]
        ans = ans + ans
        return ans