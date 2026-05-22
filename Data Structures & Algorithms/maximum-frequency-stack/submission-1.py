class FreqStack:

    def __init__(self):
        self.stack = {} #count -> group of val {1:[1,2,3], ..}
        self.count = {}
        self.maxCount = 0
    def push(self, val: int) -> None:
        valCount = 1 + self.count.get(val, 0)
        self.count[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stack[valCount] = []
        self.stack[valCount].append(val)
    def pop(self) -> int:
        res = self.stack[self.maxCount].pop()
        self.count[res] -= 1
        if not self.stack[self.maxCount]:
            self.maxCount -= 1
        return res
    # def __init__(self):
    #     self.stack = [] #val, count
    #     self.count = {}
    # def push(self, val: int) -> None:
    #     if val not in self.count:
    #         self.count[val] = 1
    #     else:
    #         self.count[val] += 1
    #     self.stack.append([val, self.count[val]])

    # def pop(self) -> int:
    #     freq = max(self.count.values())
    #     for i in range(len(self.stack) - 1, -1, -1):
    #         if freq == self.stack[i][1]:
    #             val = self.stack[i][0]
    #             self.stack.pop(i)
    #             self.count[val] -= 1
    #             return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()