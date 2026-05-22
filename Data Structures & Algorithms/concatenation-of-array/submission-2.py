class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(len(nums)):
            ans[i] = nums[i]
        ans = 2 * ans
        return ans

        # ans = []
        # for i in range(2):
        #     for n in nums:
        #         ans.append(n)
        # return ans