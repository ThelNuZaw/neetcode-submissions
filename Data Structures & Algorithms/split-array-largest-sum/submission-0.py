class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        res = right

        def canSplit(middle):
            subarray = 0
            cursum = 0
            for n in nums:
                cursum += n
                if cursum > middle:
                    subarray += 1
                    cursum = n
            return subarray + 1 <= k

        while left <= right:
            middle = (left + right) // 2
            if canSplit(middle):
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        return res