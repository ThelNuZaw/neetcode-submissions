class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # index + 1 = number exists
        #number - 1 = index >> make it negative to mark the number exists in the array.

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                index = val - 1
                if nums[index] > 0:
                    nums[index] *= -1
                elif nums[index] == 0:
                    nums[index] = -1 * (len(nums) + 1)

        for num in range(1, len(nums) + 1):
            if nums[num - 1] >= 0:
                return num
        return len(nums) + 1
        