class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # res = []
        # part = []
        # wordDict = set(wordDict)

        # def backtrack(i):
        #     if i == len(s):
        #         res.append(" ".join(part))
        #         return
        #     for j in range(i, len(s)):
        #         word = s[i : j + 1]
        #         if word in wordDict:
        #             part.append(word)
        #             backtrack(j + 1)
        #             part.pop()
                

        # backtrack(0)
        # return res
        
        wordDict = set(wordDict)
        def backtrack(i):
            if i == len(s):
                return [""]
            res = []
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word not in wordDict:
                    continue
                string = backtrack(j + 1)
                if not string:
                    continue
                for substr in string:
                    sentence = word
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            return res
        return backtrack(0)
