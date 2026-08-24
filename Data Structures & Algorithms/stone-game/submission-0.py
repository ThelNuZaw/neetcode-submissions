class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            alice_turn = True if (r - l + 1) % 2 else False #how many piles left
            left = piles[l] if alice_turn else 0
            right = piles[r] if alice_turn else 0

            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)#if Alice pick from left # if Alice pick from right
            return dp[(l, r)]
        return dfs(0, len(piles) -1) > sum(piles)// 2