class Solution:
    def climbStairs(self, n: int) -> int:
        #top-down(memorization) start 0 step to reach n with different ways
        mem = [-1] * n
        def dfs(step):
            if step >= n:
                return step == n
            if mem[step] != -1:
                return mem[step]
            mem[step] = dfs(step + 1) + dfs(step + 2)
            return mem[step]
        return dfs(0)
