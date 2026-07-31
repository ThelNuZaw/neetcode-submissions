class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            # two choice: either include current one or skip it
            newdp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                newdp.add(t + nums[i])
                newdp.add(t)
            dp = newdp
        return True if target in dp else False
