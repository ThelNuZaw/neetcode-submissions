class TimeMap:

    def __init__(self):
        self.storing = {} #using dict for key:[value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storing:
            self.storing[key] = []
        self.storing[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.storing.get(key,[])
        left = 0
        right = len(values) - 1
        answer = ""
        while left <= right:
            middle = (left + right) // 2
            if(values[middle][1] <= timestamp):
                answer = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return answer
                

        
