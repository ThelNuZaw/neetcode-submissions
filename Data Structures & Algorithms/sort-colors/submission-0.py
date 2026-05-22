class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        i = 0
        for key in range(3):
            while count[key] > 0:
                nums[i] = key
                count[key] -= 1
                i += 1
                
        