class LRUCache:

    def __init__(self, capacity: int):
       self.cache = []
       self.capacity = capacity
    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                k, v = self.cache.pop(i)
                self.cache.append([k,v])
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                k, v = self.cache.pop(i)
                v = value
                self.cache.append([k,v])
                return
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key, value])
     
