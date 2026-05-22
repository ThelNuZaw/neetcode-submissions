class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def findingpattern(s, opencount, closecount) -> None:
            if len(s) == 2 * n:
                stack.append(s)
            if opencount < n:
                findingpattern(s + '(', opencount + 1, closecount)
            if closecount < opencount:
                findingpattern(s + ')', opencount, closecount + 1)

        findingpattern("", 0, 0)
        return stack

        