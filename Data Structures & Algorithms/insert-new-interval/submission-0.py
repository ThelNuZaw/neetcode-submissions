class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = [] 
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # new end < current start
                output.append(newInterval) # we can insert before the current interval
                return output + intervals[i : ]
            elif newInterval[0] > intervals[i][1]: #new start > current end
                output.append(intervals[i])
            else: # new start < current end or new end > current start
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        output.append(newInterval)
        return output