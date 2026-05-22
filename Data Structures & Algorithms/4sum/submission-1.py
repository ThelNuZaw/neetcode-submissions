class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i]== nums[i-1]:
        #         continue
        #     for j in range(i + 1, len(nums)):
        #         if j > i + 1 and nums[j] == nums[j-1]:
        #             continue
        #         l = j + 1
        #         r = len(nums) - 1
        #         while l < r:
        #             sum4 = nums[i] + nums[j] + nums[l] + nums[r]
        #             if sum4 > target:
        #                 r -= 1
        #             elif sum4 < target:
        #                 l += 1
        #             else:
        #                 res.append([nums[i], nums[j], nums[l], nums[r]])
        #                 l += 1
        #                 while l < r and nums[l] == nums[l - 1]:
        #                     l += 1
        # return res
            
        q = []
        res = []
        nums.sort()
        def ksum(k, s, t):
            if k != 2:
                for i in range(s, len(nums) - k + 1):
                    if i > s and nums[i] == nums[i -1]:
                        continue
                    q.append(nums[i])
                    ksum(k-1, i + 1, t - nums[i])
                    q.pop()
                return 
            l = s
            r = len(nums) - 1
            while l < r:
                sub = nums[l] + nums[r]
                if sub > t:
                    r -= 1
                elif sub < t:
                    l += 1
                else:
                    res.append(q + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        ksum(4, 0, target)
        return res
