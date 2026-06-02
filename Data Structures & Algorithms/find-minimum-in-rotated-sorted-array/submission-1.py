class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minnum = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                minnum = min(minnum, nums[left])
                break
            
            middle = (left + right) // 2
            minnum = min(minnum, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return minnum