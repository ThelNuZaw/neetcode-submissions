class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, start):
            if start >= len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[start])
            dfs(path, start + 1)
            path.pop()
            dfs(path, start + 1)


        dfs([], 0)

        return res