class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        arr = []
        
        while left <= right:
            middle = (left + right) // 2
            res = 0
            for i in range(len(piles)):
                res += math.ceil(piles[i] / middle)
            if res > h:
                left = middle + 1
            else:
                arr.append(middle)
                right = middle - 1
        return(min(arr))
