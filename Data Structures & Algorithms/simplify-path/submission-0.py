class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        newpath = path.split("/") #return list
        for p in newpath:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "" and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)