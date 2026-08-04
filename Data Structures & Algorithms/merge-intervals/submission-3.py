class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = output[-1]
            current = intervals[i]
            if current[0] > prev[1]: #current start > prev end
                output.append(current)
            else:
                prev[0] = min(prev[0], current[0])
                prev[1] = max(prev[1], current[1])
        return output