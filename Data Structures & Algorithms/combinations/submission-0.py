class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(num, path):
            if len(path) == k:
                res.append(path.copy())
                return
            if num > n:
                return 
            path.append(num)
            dfs(num + 1, path)
            path.pop()
            dfs(num + 1, path)
        dfs(1,[])
        return res