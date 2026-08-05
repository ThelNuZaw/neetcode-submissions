class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1] #keep track the end time of each interval
        for start, end in intervals[1:]:
            if start >= prevEnd: #non-overlaping
                prevEnd = end
            else:
                res += 1 #overlapping
                prevEnd = min(end, prevEnd) #want to remove the greater end time
        return res