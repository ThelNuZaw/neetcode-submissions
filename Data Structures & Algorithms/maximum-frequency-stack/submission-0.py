class FreqStack:

    def __init__(self):
        self.stack = [] #val, count
        self.count = {}
    def push(self, val: int) -> None:
        if val not in self.count:
            self.count[val] = 1
        else:
            self.count[val] += 1
        self.stack.append([val, self.count[val]])

    def pop(self) -> int:
        freq = max(self.count.values())
        for i in range(len(self.stack) - 1, -1, -1):
            if freq == self.stack[i][1]:
                val = self.stack[i][0]
                self.stack.pop(i)
                self.count[val] -= 1
                return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()