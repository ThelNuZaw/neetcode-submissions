class Solution:
    def maxArea(self, heights: List[int]) -> int:
        count = 0
        result = []
        left, right = 0, len(heights) -1
        while(left < right):
            index = right - left
            if(heights[left] <= heights[right]):
                current = heights[left]
                left += 1
            else:
                current = heights[right]
                right -= 1
            count = current * index   
            result.append(count)
            
        return(max(result))
                
        