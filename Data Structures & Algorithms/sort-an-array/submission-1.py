class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    #     for i in range(1,len(nums)):
    #         key = nums[i]
    #         j = i - 1

    #         while j >= 0 and key < nums[j]:
    #             nums[j+1] = nums[j]
    #             j-= 1
    #         nums[j+1] = key
    #     return nums

        def countingsort():
            count = defaultdict(int)
            maxValue = max(nums)
            minValue = min(nums)
            for key in nums:
                count[key] += 1
            
            i = 0
            for key in range(minValue, maxValue + 1):
                while count[key] > 0:
                    nums[i] = key
                    count[key] -=1
                    i += 1

        countingsort()
        return nums 
