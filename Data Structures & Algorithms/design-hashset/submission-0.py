class MyHashSet:

    def __init__(self):
        self.array = []

    def add(self, key: int) -> None:
        if key not in self.array:
            self.array.append(key)

    def remove(self, key: int) -> None:
        if key in self.array:
            self.array.remove(key)

    def contains(self, key: int) -> bool:
        if key not in self.array:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)