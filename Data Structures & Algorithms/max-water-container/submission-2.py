class Solution:
    def maxArea(self, heights: List[int]) -> int:
        marea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            a = (r - l) * min(heights[l], heights[r])
            marea = max(marea, a)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
        return marea
        