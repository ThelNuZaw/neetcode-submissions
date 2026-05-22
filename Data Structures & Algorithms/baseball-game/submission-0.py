class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ans = 0
        for i, op in enumerate(operations):
            if op == '+':
                total = res[-1] + res[-2]
                res.append(total)
            elif op == 'C':
                res.pop()
            elif op == 'D':
                mul = res[-1] * 2
                res.append(mul)
            else:
                res.append(int(op))
        return sum(res)
        