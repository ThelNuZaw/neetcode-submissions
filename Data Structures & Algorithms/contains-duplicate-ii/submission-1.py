class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window = set()
        # L = 0
        # for R in range(len(nums)):
        #     if R - L > k:
        #         window.remove(nums[L])
        #         L += 1
        #     if nums[R] in window:
        #         return True
        #     window.add(nums[R])
        # return False

        #hashmap
        seen = {}
        for i, n in enumerate(nums):
            if nums[i] in seen and i - seen[n] <= k:
                return True
            seen[n] = i
        return False
                    