class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
           
            while stack:
                ptemp, pindex = stack[-1]
                if temp > ptemp:
                    stack.pop()
                    result[pindex] = i - pindex
                else:
                    break
            stack.append((temp,i))
            
        return result