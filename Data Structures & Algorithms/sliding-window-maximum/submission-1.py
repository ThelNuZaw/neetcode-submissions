class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        q = collections.deque() # store index
        output = []

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]: # when nums window is decreasing order and cannot remove old indices 
                            # by larger value before window is invalid window = [5,3,2,1]
                q.popleft()
            if right + 1 >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1
        return output