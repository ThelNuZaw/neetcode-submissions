class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        maxL = height[l]
        maxR = height[r]
        if not height:
            return 0
        while l < r:
            
            if maxL < maxR:
                l += 1
                
                maxL = max(maxL, height[l])
                area += maxL - height[l] # for positive value adding
               
            else:
                r -= 1
                
                maxR = max(maxR, height[r])
                area += maxR - height[r]
               
        return area

        