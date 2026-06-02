class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        capacity = right
        while left <= right:
            curload = 0
            dayneeded = 1
            middle = (left + right) // 2
            for w in weights:
                curload += w
                if curload > middle:
                    dayneeded += 1
                    curload = w
            if dayneeded <= days:
                right = middle - 1
                capacity = min(capacity, middle)
            else:
                left = middle + 1
        return capacity
