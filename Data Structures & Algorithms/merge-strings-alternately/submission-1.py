class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        l1 = 0
        l2 = 0
        i = 0
        while l1 < len(word1) and l2 < len(word2):
            output.append(word1[l1])
            output.append(word2[l2])
            l1+= 1
            l2 += 1
        output.append(word1[l1:])
        output.append(word2[l2:])
        return "".join(output)