class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl = 0
        for n in nums:
            if n-1 not in nums:
                maxlength = 1
                while n + maxlength in nums:
                    maxlength += 1
                maxl = max(maxl, maxlength)
        return maxl