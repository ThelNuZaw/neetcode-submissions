class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if nums[middle] >= nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

