class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in temp:
                return [temp[difference], i]
            else:
                temp[n] =i                    
        