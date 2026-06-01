class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            middle = (left + right) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p/middle)
            if hour <= h:
                res = min(res,middle)
                right = middle - 1
            else:
                left = middle + 1
        return res
            