class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
       
        dToc = {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"}

        def dfs(i, curS):
            if len(curS) == len(digits):
                res.append(curS)
                return
            for c in dToc[digits[i]]: # loop through "abc" if "2"
                
                dfs(i + 1, curS + c)
        if digits:
            dfs(0, "")
        return res