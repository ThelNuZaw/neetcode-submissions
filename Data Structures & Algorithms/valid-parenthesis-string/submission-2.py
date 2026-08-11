class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, p in enumerate(s):
            if p == "(":
                left_stack.append(i)
            elif p == "*":
                star_stack.append(i)
            else: # p ==")"
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop() #treat it as "("
                else:
                    return False
        #in some situations, some "(" can still be unmatched
        #try to match with "*"
        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False
        return True if not left_stack else False