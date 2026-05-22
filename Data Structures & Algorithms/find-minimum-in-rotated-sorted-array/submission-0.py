class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        answer = nums[0]
        while left <= right:
            if(nums[left] < nums[right]):
                answer = min(answer, nums[left])
                break

            middle = (left + right) // 2
            answer = min(answer, nums[middle])
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return(answer)
            
            