class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        goal = len_nums - 1
        
        for cur in range(len_nums - 2, -1, -1):
            jump = goal - cur
            if(nums[cur] >= jump):
                goal = cur
            
        if(goal != 0):
            return False
        return True          

        
        