class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        total = mountainArr.length()

        #find peak
        l, r = 1, total - 2 # maked sure peak is not on the edges
        while l <= r:
            m = (l + r) // 2
            left = mountainArr.get(m - 1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        #find target in left segment which is in increasing order
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            v = mountainArr.get(m)
            if v < target:
                l = m + 1
            elif v > target:
                r = m - 1
            else:
                return m
        
        #find target in right segment which is in decreasing order
        l, r = peak, total - 1
        while l <= r:
            m = (l + r) // 2
            v = mountainArr.get(m)
            if v < target:
                r = m - 1
            elif v > target:
                l = m + 1
            else:
                return m

        return -1