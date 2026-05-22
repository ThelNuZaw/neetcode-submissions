class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        output = 0
        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                res.append(int(t))
            else:
                first = res.pop()
                second = res.pop()
                if t == '+':
                    output = second + first
                    
                elif t == '-':
                    output = second - first
                    
                elif t == '*':
                    output = first * second
                    
                else:
                    output = int(second / first)
                res.append(output)
        return res.pop()