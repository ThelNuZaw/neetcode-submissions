class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
       
        for i in range(len(tokens)):
            sign = tokens[i]
            if sign not in {'+', '-', '*', '/'}:
                operand = int(sign)
                stack.append(operand)
            else:
                first = stack.pop()
                last = stack.pop()
                if sign == '+':
                    result = last + first
                elif sign == '-':
                    result = last - first
                elif sign == '*':
                    result = last * first
                else:
                    result = int(last / first)
                stack.append(result)
            i = i + 1
        return stack.pop()             
        