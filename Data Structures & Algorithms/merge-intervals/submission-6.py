class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
                output[-1][0] = min(start, output[-1][0])
                

            else:
                output.append([start, end])
        return output
                