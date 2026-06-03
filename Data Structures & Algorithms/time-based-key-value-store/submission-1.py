class TimeMap:

    def __init__(self):
        self.main = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.main:
            self.main[key] = []
        self.main[key].append([value, timestamp])
       
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.main.get(key, [])
        left = 0
        right = len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res  