class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isPair = True
        i = 0
        while i < len(s) and isPair:
            tag = s[i]
            if tag in "({[":
                stack.append(tag)
            else:
                if not stack:
                    isPair = False
                else:
                    checkpair = stack.pop()
                    matches = {')': '(', ']': '[', '}': '{'}
                    if (checkpair!= matches[tag]):
                        isPair = False
            i = i + 1
        if len(stack) == 0 and isPair:
            return True
        else:
            return False
    
                       
                    