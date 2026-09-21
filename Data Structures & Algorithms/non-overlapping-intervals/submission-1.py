class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        delete = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                delete += 1
                prevEnd = min(prevEnd, end) # want to keep the earlier end time so that avoid overlapping
        return delete