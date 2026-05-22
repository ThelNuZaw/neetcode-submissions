class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for en in s:
            if en != ']':
                stack.append(en)
            else:
                string = ""
                while stack and stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                d = ""
                while stack and stack[-1].isdigit():
                    d = stack.pop() + d
                    mul = int(d)
                stack.append(mul * string)
        return "".join(stack)