class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, s):
            if s == target:
                res.append(cur.copy())
                return 
            if i >= len(nums) or s > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, s + nums[i])
            cur.pop()
            dfs(i + 1, cur, s)
        dfs(0, [], 0)
        return res