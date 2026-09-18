"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals) - 1):
            first = intervals[i]
            for j in range(i + 1, len(intervals)):
                second = intervals[j]
                if first.end > second.start and first.start < second.end:
                    return False
        return True