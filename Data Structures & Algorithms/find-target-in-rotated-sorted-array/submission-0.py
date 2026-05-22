class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            if(nums[middle] >= nums[left]):
                if(target > nums[middle]):
                    left = middle + 1
                else:
                    if(target < nums[left]):
                        left = middle + 1
                    else:
                        right = middle - 1
            else:
                if(target < nums[middle]):
                    right = middle - 1
                else:
                    if(target > nums[right]):
                        right = middle - 1
                    else:
                        left = middle + 1
        return -1

