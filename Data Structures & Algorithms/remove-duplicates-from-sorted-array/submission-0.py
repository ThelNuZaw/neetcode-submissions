class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while left <= right and right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left += 1
                right += 1
        return len(nums)
