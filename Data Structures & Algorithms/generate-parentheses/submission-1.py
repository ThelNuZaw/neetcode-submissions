class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(stack))
                return
            
            if open_count < n:
                stack.append("(")
                dfs(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(")")
                dfs(open_count, close_count + 1)
                stack.pop()

        dfs(0,0)
        return res